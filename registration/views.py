from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse,HttpResponseRedirect
from random import randint
import requests
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core import mail
from datetime import datetime, timedelta, date
from django.views.decorators.cache import cache_control
from django.utils import timezone
from django.utils.timezone import utc
from django.conf import settings
from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash


COMPANY_NUMBER = "+16024973298"

def contextCall(request):
	pass

#view for login page
@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signIn(request):
	# if request.user.is_authenticated():
	# 	return render(request,"dashboard.html")
	# if request.session.get_expiry_age() > 0:
	# 		request.session.set_expiry(0)
	# 		if request.user.pvuser.isProfileComplete:
	# 			first_name = request.user.first_name	
	# 			return render(request,'dashboard1.html',{'first_name':first_name})
	# 		else:
	# 			return redirect('/completeprofile/')
	if request.method == 'POST':
		form = request.POST
		print(form)
		try:
			username = User.objects.get(username = form['username'])
			print(1)
		except:	
			try:
				username = PvUser.objects.get(mobile_number = form['username']).user.username
				print(username)
				print(2)
			except:
				messages.warning(request,'Invalid Credentials!!')
				return render(request,'login.html')		
		try:
			user = authenticate(username = username, password = form['password'])
			print(user.pvuser)
			if user is not None:
	    	# the password verified for the user
				if user.is_active:
					# print(3)
					login(request,user) 
					if user.pvuser.isProfileComplete:
						if 'remember_me' in form:
							request.session[settings.KEEP_LOGGED_KEY] = True
						first_name = user.first_name	
						return render(request,'dashboard1.html',{'first_name':first_name})
					else:
						return redirect('/completeprofile/')
				else:
					messages.warning(request,"The account is disabled. please activate your account.")
			else:
				print(4)
				messages.warning(request,"Invalid Credentials !!!")
#			user = User.objects.get(username=form['username'],password=form['password'])
#			print("user is found")
			return render(request,'login.html')
				
		except:
			print("user is not found,please create account!!")	
			return render(request,'login.html')
	else:		 
		return render(request,'login.html')


@csrf_exempt
#View for registration page
def register(request):
	# if request.user.is_authenticated():
	# 	return redirect("/login")
	response = {}
	if request.method == 'POST':
		form = request.POST
		first_name = form["first_name"]
		last_name = form["last_name"]
		email = form["email"]
		aadhar_no = form["aadhar"]
		mobile_number = str(form["mobile_number"])
		password = form["password"]
		activationToken = str(randomWithNDigits(8))
		lastUserId = User.objects.latest('id').id
		vhn = "VHN"+str(100000+lastUserId+1)
		try:
			try:
				print('code base 0')
				PvUser.objects.get(mobile_number = mobile_number)
				messages.warning(request,"User already registered with this Mobile Number.")
				return render(request, 'register.html')
				# response['status'] = 1
				# return JsonResponse(response) #User already registered with this mobile number
			except:
				print("code base 1")
				# print(sendSms('+91'+str(mobile_number),"Thanks for registering at vyala.Your unique VHN Number is "+vhn+". Use OTP "+activationToken+" to activate your account.OTP is valid for 3 minutes."))				
		except:
			print("code base 2")
			messages.warning(request,"Connection problem or Invalid Phone Number !!!")
			return render(request, 'register.html')
			# response['status'] = 0
			# return JsonResponse(response) #connection problem or invalid phone number
		user = User.objects.create_user(
			username=vhn,
			first_name=first_name,
			last_name=last_name,
			password=password,)
		pvUser = PvUser.objects.get_or_create(
			email=email,
			aadhar_no = aadhar_no,
			mobile_number=mobile_number,
			activationToken = activationToken,
			user = user,
			pTime = datetime.utcnow().replace(tzinfo = utc))
		# if email:
		# 	try:
		# 		subject = "Welcome To Vyala Family"
		# 		body = "You have successfully registered at vyala and Your VHN Number is "+ vhn
		# 		sendEmail(email,subject,body)
		# 	except:
		# 		messages.warning('connection problem or invalid email!!')
		# 		return render(request,'register.html')	
		return render(request,'is_OTPvalid.html',{'vhn' : vhn})
		# response['vhn'] = vhn
		# response['status'] = 3 #OTP sent successfully and redirected to otp validation page
		# return JsonResponse(response)
	else:
		# form = RegistrationForm()
        
		return render(request,'register.html')

#View for OTP validation
@csrf_exempt
def OTPvalidation(request):
	if request.method == 'POST':
		form = request.POST
		try:
			user = User.objects.get(username = form['vhn'])
			pvUser = user.pvuser
		except:
			messages.warning(request,"Entered VHN number does not exist.")
			return render(request,"is_OTPvalid.html",{'vhn':form['vhn']})
		if not pvUser.otpValidTime(3):
			messages.warning(request,"Plese resend OTP, OTP is expired now.")
			return render(request,"is_OTPvalid.html",{'vhn':form['vhn']})	
		if form["OTP"] == pvUser.activationToken:
			user.is_active = True
			pvUser.activeYesNo = True
			pvUser.activationToken = None
			pvUser.activationAttempts += 1
			pvUser.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request,user)
			return redirect('/completeprofile/')
		else:
			pvUser.activationAttempts += 1
			if pvUser.activationAttempts > 3:
				messages.warning(request,'Maybe you have entered wrong phone number. Please register again.')
				pvUser.delete()
				return render(request,'register.html')
			pvUser.save()
			messages.warning(request,'Please enter correct OTP !!')
			return render(request,'is_OTPvalid.html',{'vhn':form['vhn']})	
	else:
		return render(request,'is_OTPvalid.html')	

#view for otpresend request
def resendOTP(request):
	response = {}
	if request.method == 'POST':
		form = request.POST
		activationToken = str(randomWithNDigits(8))
		try:
			user = User.objects.get(username = form['vhn'])
			pvUser = user.pvuser
		except:
			messages.warning(request,'Invalid VHN number')
			response['status'] = 2 # INvalid VHN Number
			return JsonResponse(response)
		try:
			#sendSms("+91"+str(pvUser.mobile_number),"Thanks for registering at vyala.Your unique VHN Number is "+str(form['vhn'])+". Use OTP "+activationToken+" to activate you account.OTP is valid for 3 minutes.")
			pvUser.pTime = pTime = datetime.utcnow().replace(tzinfo = utc)
			pvUser.activationToken = activationToken
			pvUser.save()
			response['status'] = 1 
			return JsonResponse(response)
		except:
			response['status'] = 0 ### connection error or unknown error
			return JsonResponse(response)
	else:
		response['status'] = "Invalid!!"
		return JsonResponse(response)


#view for finding account and sending otp on registered mobile number
@csrf_exempt
def FindAccount(request):
	response={}
	if request.method == 'POST':
		form = request.POST
		activationToken = str(randomWithNDigits(8))
		try:
			user = User.objects.get(username = form['VHN'])
			pvUser = user.pvuser
			if not pvUser.otpValidTime(3):
				messages.warning(request,"Plese resend OTP, OTP is expired now.")
			if form['OTP']:
				if form['OTP'] == pvUser.activationToken:
					print(5)
					response['status'] = 5 
					response['vhn'] = str(form['VHN'])
					user.backend = 'django.contrib.auth.backends.ModelBackend'
					login(request,user)
					return JsonResponse(response)
				else:
					response['status']=3
					return JsonResponse(response)
			else:		
				try :
					mobileNumber = "+91"+str(pvUser.mobile_number) 
					print(mobileNumber)
					#sendSms(mobileNumber,"Your Vyala OTP to set password is: "+activationToken)
					pvUser.pTime = pTime = datetime.utcnow().replace(tzinfo = utc)
					pvUser.activationToken = activationToken
					pvUser.save()
					response['status'] = 1 
					return JsonResponse(response)
				except:
					response['status'] = 0 ### connection error or unknown error
					return JsonResponse(response)				
		except:
			response['status'] = 2 # INvalid VHN Number
			return JsonResponse(response)
		
	else:
		return render(request,'FindAccount.html')

@csrf_exempt
def ActivateAccount(request):
	response={}
	if request.method == 'POST':
		form = request.POST
		activationToken = str(randomWithNDigits(8))
		try:
			user = User.objects.get(username = form['VHN'])
			pvUser = user.pvuser
			print(1)
			if not pvUser.otpValidTime(3):
				messages.warning(request,"Plese resend OTP, OTP is expired now.")
			if form['OTP']:
				print(2)
				if form['OTP'] == pvUser.activationToken:
					print(form['OTP'])
					pvUser.user.is_active=True
					pvUser.activeYesNo = True
					pvUser.save()
					messages.success(request,'Congratulations !! Your account is activated.')
					response['status']=4
					return JsonResponse(response)
				else:
					response['status']=3
					return JsonResponse(response)
			else:		
				try :
					mobileNumber = "+91"+str(pvUser.mobile_number) 
					print(mobileNumber)
					#sendSms(mobileNumber,"Use OTP: "+activationToken + "to activate your account.")
					pvUser.pTime = pTime = datetime.utcnow().replace(tzinfo = utc)
					pvUser.activationToken = activationToken
					pvUser.save()
					response['status'] = 1 
					return JsonResponse(response)
				except:
					response['status'] = 0 ### connection error or unknown error
					return JsonResponse(response)				
		except:
			response['status'] = 2 # INvalid VHN Number
			return JsonResponse(response)			
	else:
		return render(request,'ActivateAccount.html')

#view to reset password	
@login_required(login_url = "/login")	
def SetPassword(request,pvUser):
	response = {}
	if request.method == 'POST':
		form = request.POST
		pv = User.objects.get(username = pvUser)
		pv.set_password(form['password'])
		pv.save()
		messages.success(request,'Password is successfully set.')
		return redirect('/login/')
	else:
		return render(request,'SetPassword.html',{"vhn":pvUser})	

#view for changing passsword
@csrf_exempt
@login_required(login_url = "/login")
def changePass(request):
	response={}
	username = None
	# if request.user.is_authenticated():
	username = request.user.username
	if request.method == 'POST':
		form = request.POST
		print(str(request.POST))
		if form['currentPass']:
			newUser = authenticate(username = username, password = form['currentPass'])
			if newUser is not None:
				if form['newPass']:
					user = User.objects.get(username=username)
					user.set_password(form['newPass'])
					user.save()
					response['status']=3 # Password Changed Successfully
					return JsonResponse(response)
				else:
					response['status'] = 4 # now show new Password button
					return JsonResponse(response)
			else:
				response['status']=2 # wrong currentPassword
				return JsonResponse(response)				

	else:
		print(1)
		response['status']=1
		return JsonResponse(response)	
	# else:
	# 	response['status']=4
	# 	return JsonResponse(response)	

@login_required(login_url = "/login/")
@csrf_exempt
def profile(request):
	response = {}
	username = None
	d={}
	if request.method == 'POST':
		relative_names = None
		relations = None
		relative_vhnNumbers = None
		medical_history = None
		family_history = ['High_Blood_Pressure','Autism']
		relationship = None
		surgical_history = None
		username = request.user.username
		user = User.objects.get(username = username)
		pvUser = user.pvuser
		form = request.POST.copy()

		print(form)

		country = form['country']
		state = form['state']
		city = form['city']
		gender = form['gender']
		relative_names = form.getlist('relative-name')
		#print(relative_names) 
		relations = form.getlist('relation')
		#print(relations)
		relative_vhnNumbers = form.getlist('relative-vhnNumber')
		#print(relative_vhnNumbers)
		medical_history = form.getlist('medicalHistory')
		#print(medical_history)
		surgical_history = form.getlist('surgicalHistory')
		#print(surgical_history)
		# familyhistory_objects = FamilyhistoryMaster.objects.all()
		# for var in familyhistory_objects:
		# 	family_history.append(var.name)
		# 	print(family_history)
		family_history += form.getlist('disease')
		print(family_history)
		relationship = form.getlist('relationship')
		print(relationship)
		if 'drinks/week' not in form:
			form['drinks/week'] = 0
		if 'whenTobacoLeft' not in form:
			form['whenTobacoLeft'] = 'no tobacco'
		if 'drugDetails' not in form:
			form['drugDetails'] = 'no drugs'
		if 'drugQuitDate' not in form:
			form['whenDrugLeft'] = 'no drugs'

		try:
			d["{0}".format(country)] = CountryMaster.objects.get(name = country)
		except:	
			print(country)
			d["{0}".format(country)] = CountryMaster(name = form['country'], activeYesNo = True, lastModifiedDateTime = timezone.now())
			d["{0}".format(country)].save()
		try:
			d["{0}".format(state)] = StateMaster.objects.get(name = state)
		except:	
			#print(state)
			d["{0}".format(state)] = StateMaster(name = form['state'], activeYesNo = True, lastModifiedDateTime = timezone.now(), country = d["{0}".format(country)])	
			d["{0}".format(state)].save()
		try:
			d["{0}".format(city)] = CityMaster.objects.get(name = city)
		except:	
			#print(city)
			d["{0}".format(city)] = CityMaster(name = form['city'], activeYesNo = True, lastModifiedDateTime = timezone.now(), state = d["{0}".format(state)])
			d["{0}".format(city)].save()
		try:
			d["{0}".format(gender)] = GenderMaster.objects.get(name = gender)
		except:
			#print(gender)
			d["{0}".format(gender)] = GenderMaster(name = form['gender'], activeYesNo = True, lastModifiedDateTime = timezone.now())
			d["{0}".format(gender)].save()
		for relation in relations:
			#print(1)
			try:
				d["{0}".format(relation)] = RelationshipMaster.objects.get(name = relation)
			except:
				#print(relation)	
				d["{0}".format(relation)] = RelationshipMaster(name = relation, activeYesNo = True, lastModifiedDateTime = timezone.now())
				d["{0}".format(relation)].save()
		for medhistory in medical_history:
			try:
				d["{0}".format(medhistory)] = MedicalhistoryMaster.objects.get(name = medhistory)
			except:
				#print(medhistory)	
				d["{0}".format(medhistory)] = MedicalhistoryMaster(name = medhistory, activeYesNo = False, lastModifiedDateTime = timezone.now())
				d["{0}".format(medhistory)].save()
		for surhistory in surgical_history:
			try:
				d["{0}".format(surhistory)] = SurgicalhistoryMaster.objects.get(name = surhistory)
			except:
				#print(surhistory)	
				d["{0}".format(surhistory)] = SurgicalhistoryMaster(name = surhistory, activeYesNo =False, lastModifiedDateTime = timezone.now())
				d["{0}".format(surhistory)].save()

		for famhistory in family_history:
			try:
				d["{0}".format(famhistory)] = FamilyhistoryMaster.objects.get(name = famhistory)
			except:
				#print(famhistory)	
				d["{0}".format(famhistory)] = FamilyhistoryMaster(name = famhistory, activeYesNo =False, lastModifiedDateTime = timezone.now())
				d["{0}".format(famhistory)].save()
		
					
		pvProfile = PvProfile.objects.get_or_create(
			userId = pvUser,
			countryId = d["{0}".format(country)],
			stateId = d["{0}".format(state)],
			cityId = d["{0}".format(city)],
			# profilePhoto = request.FILES['profilePic'],
			address = form['address'],
			dob = form['DOB'],
			gender = d["{0}".format(gender)],
			lastModifiedDateTime = timezone.now(),
			)
		
		i=0
		for relative in relative_names:
			user = User.objects.get(username = relative_vhnNumbers[i])
			pvUser = user.pvuser
			pvFamilyRelationship = PvFamilyRelationship.objects.get_or_create(
				patientId = pvUser,
				relativeName = relative,
				relationshipId = d["{0}".format(relations[i])],
				relative = pvUser,
				lastModifiedDateTime = timezone.now())
			i+=1

		pvSocialHistory = PvSocialHistory.objects.get_or_create(
			patientId = pvUser,
			alcoholUsage = form['acheck'],
			drinksPerWeek = form['drinks/week'],	
			tobacoUsage = form['tcheck'],
			tobacoQuitDate = form['whenTobacoLeft'],
			drugUsage = form['dcheck'],
			# drugQuitDate = form['whenDrugLeft'],
			drugDetails = form['drugDetails'])

		for medhistory in medical_history:
			pvMedicalHistory = PvMedicalHistory.objects.get_or_create(
				patientId = pvUser,
				mediacalHistoryId = d["{0}".format(medhistory)],
				lastModifiedDateTime = timezone.now())

		for surhistory in surgical_history:
			pvSurgicalHistory = PvSurgicalHistory.objects.get_or_create(
				patientId = pvUser,
				surgicalhistoryId = d["{0}".format(surhistory)],
				lastModifiedDateTime = timezone.now())
		i=0
		x=None
		for famhistory in family_history:
			if i==0:
				x = form['table_records_hbp']
			if i==1:
				x = form['table_records_aut']
			pvFamilyHistory = PvFamilyHistory.objects.get_or_create(
				patientId = pvUser,
				familyhistoryId = d["{0}".format(famhistory)],
				familyhistoryStatus = x,	
				relationshipId = RelationshipMaster.objects.get(name=relationship[i]),
				lastModifiedDateTime = timezone.now())	
			i += 1

		# messages.success(request,'saved')
		pvUser.isProfileComplete = True
		return render(request,'dashboard1.html',{'first_name':user.first_name})
		
	else:
		pvUser = request.user
		print(pvUser)
		historys = FamilyhistoryMaster.objects.all()
		relations = RelationshipMaster.objects.all()
		countries = CountryMaster.objects.all()
		states = StateMaster.objects.all()
		cities = CityMaster.objects.all()
		return render(request,'profile.html',{'historys':historys,'relations':relations,'countries':countries,'states':states,'cities':cities,'user':pvUser})

# def relationship(request):
# 	response = {}
# 	if request.method == 'POST':
# 		# pvUser = request.user.pvuser
# 		# form = request.POST
# 		i=0
# 		d={}
# 		relative_names = None
# 		relations = None
# 		relative_vhnNumbers = None
# 		relative_names = form.getlist('relative-name')
# 		print(relative_names) 
# 		relations = form.getlist('relation')
# 		print(relations)
# 		relative_vhnNumbers = form.getlist('relative-vhnNumber')
# 		print(relative_vhnNumbers)
# 		for relation in relations:
# 			print(1)
# 			try:
# 				d["{0}".format(relation)] = RelationshipMaster.objects.get(name = relation)
# 			except:
# 				print(relation)	
# 				d["{0}".format(relation)] = RelationshipMaster(name = relation, activeYesNo = True, lastModifiedDateTime = timezone.now())
# 				d["{0}".format(relation)].save()
# 		for relative in relative_names:
# 			user = User.objects.get(username = relative_vhnNumbers[i])
# 			pvUser = user.pvuser
# 			pvFamilyRelationship = PvFamilyRelationship.objects.get_or_create(
# 				# patientId = pvUser,
# 				relativeName = relative,
# 				relationshipId = d["{0}".format(relations[i])],
# 				relative = pvUser,
# 				lastModifiedDateTime = timezone.now())
# 	else:
# 		return HttpResponse('error 403')

# def medicalHistory(request):
# 	# username = request.user.username
# 	if request.method == 'POST':
# 		medical_history = None
# 		d={}
# 		# user = User.objects.get(username = username)
# 		# pvUser = user.pvuser
# 		form = request.POST
# 		medical_history = form.getlist('medicalHistory')
# 		print(medical_history)
# 		for medhistory in medical_history:
# 			try:
# 				d["{0}".format(medhistory)] = MedicalhistoryMaster.objects.get(name = medhistory)
# 			except:
# 				print(medhistory)	
# 				d["{0}".format(medhistory)] = MedicalhistoryMaster(name = medhistory, activeYesNo = False, lastModifiedDateTime = timezone.now())
# 				d["{0}".format(medhistory)].save()
# 		for medhistory in medical_history:
# 			pvMedicalHistory = PvMedicalHistory.objects.get_or_create(
# 				# patientId = pvUser,
# 				mediacalHistoryId = d["{0}".format(medhistory)],
# 				lastModifiedDateTime = timezone.now())					

# 	else:
# 		return HttpResponse('403 bad request')	

# def surgicalHistory(request):
# 	# username = None
# 	# username = request.user.username
# 	if request.method == 'POST':
# 		# user = User.objects.get(username = username)
# 		# pvUser = user.pvuser
# 		form = request.POST
# 		for surhistory in surgical_history:
# 			try:
# 				d["{0}".format(surhistory)] = SurgicalhistoryMaster.objects.get(name = surhistory)
# 			except:
# 				print(surhistory)	
# 				d["{0}".format(surhistory)] = SurgicalhistoryMaster(name = surhistory, activeYesNo =False, lastModifiedDateTime = timezone.now())
# 				d["{0}".format(surhistory)].save()
# 		for surhistory in surgical_history:
# 			pvSurgicalHistory = PvSurgicalHistory.objects.get_or_create(
# 				# patientId = pvUser,
# 				surgicalhistoryId = d["{0}".format(surhistory)],
# 				lastModifiedDateTime = timezone.now())				

# 	else:
# 		return HttpResponse('403 bad request')

# def socialHistory(request):
# 	# username = None
# 	# username = request.user.username
# 	if request.method == 'POST':
# 		# user = User.objects.get(username = username)
# 		# pvUser = user.pvuser
# 		form = request.POST
# 		pvSocialHistory = PvSocialHistory.objects.get_or_create(
# 		# patientId = pvUser,
# 		alcoholUsage = form['acheck'],
# 		drinksPerWeek = form['drinks/week'],
# 		tobacoUsage = form['tcheck'],
# 		tobacoQuitDate = form['whenTobacoLeft'],
# 		drugUsage = form['dcheck'],
# 		drugQuitDate = form['whenDrugLeft'],
# 		drugDetails = form['drugDetails'])					

# 	else:
# 		return HttpResponse('403 bad request')											
	
@csrf_exempt
def checkRelation(request):
	i=0
	response = {}
	if request.method == 'POST':
		details = request.POST
		print(details)
		relative_names = details.getlist('relative-name[]')
		print(relative_names)
		vhn_numbers = details.getlist('relative-vhnNumber[]')
		print(vhn_numbers)
		for vhn in vhn_numbers:
			try:
				print(1)
				user = User.objects.get(username = vhn)
				respective_name = user.first_name +' '+ user.last_name
				print(respective_name)
				print(relative_names[i])
				if respective_name == relative_names[i]:
					print(3)
					i += 1
				else:
					response['status'] = 1
					response['name'] = relative_names[i]
					response['vhn']	= vhn
					i += 1
					return JsonResponse(response)
			except:
				print(0)
				response['status'] = 0
				response['name'] = relative_names[i]
				response['vhn']	 = vhn
				i += 1
				return JsonResponse(response)
		response['status'] = 2
		return JsonResponse(response)		
	else:
		return HttpResponse('error 404')			

def logout_view(request):
	logout(request)
	return redirect('/login/')

#View for sending email from zoho
def sendEmail(recipient, subject, body):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = 'naman.kansal@vyalatech.com'
	msg['To'] = recipient

	text = "Hi, You are registerd at vyala successfully"

	part1 = MIMEText(text, 'plain')

	msg.attach(part1)
	s = smtplib.SMTP_SSL('smtp.zoho.com',465)
	s.login('naman.kansal@vyalatech.com','9756089119')
	s.sendmail('naman.kansal@vyalatech.com', recipient, msg.as_string())
	s.quit()


#view for sending sms
def sendSms(recipientNumber, content):
	uname='jishnu@vyalatech.com'
	hashkey='e844056e4e3c75ace149c250f4ab998e510dd30f'
	number=recipientNumber
	msg=content
	sender='We Care'

	r = requests.post('http://api.textlocal.in/send/', data ={'username':uname,'hash':hashkey,'numbers':number,'message':msg,'sender':sender})


	data=r.json()
	# return data
	print(data['status'])

#function for generating activationToken
def randomWithNDigits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)


def relation(request):
	# form = RegistrationForm()
	return render(request,'profile.html',{'Url':gravTest("namankansal32@gmail.com")})

class KeepLoggedInMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated() or not settings.KEEP_LOGGED_KEY in request.session:
            return
        if request.session[settings.KEEP_LOGGED_KEY] != date.today():
            request.session.set_expiry(timedelta(days=settings.KEEP_LOGGED_DURATION))
            request.session[settings.KEEP_LOGGED_KEY] = date.today()
        return

