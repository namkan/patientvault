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
from datetime import datetime
from django.views.decorators.cache import cache_control
from django.utils import timezone
from django.utils.timezone import utc
COMPANY_NUMBER = "+16024973298"

def contextCall(request):
	pass

#view for login page
@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signIn(request):
	# if request.user.is_authenticated():
	# 	return render(request,"dashboard.html")
	if request.method == 'POST':
		form = request.POST
#		remember_me = form.cleaned_data["remember_me"]
		# print(form)
		# print(form['username'])
		# print(form['password'])
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
			print(user)
			if user is not None:
	    	# the password verified for the user
				if user.is_active:
					# print(3)
					login(request,user)
					#if 'remember_me' in form:
					#	request.session.set_expiry(1209600)
					first_name = user.first_name	
					return render(request,'dashboard.html',{'first_name':first_name})	
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
		mobile_number = str(form["mobile_number"])
		password = form["password"]
		activationToken = str(randomWithNDigits(8))
		lastUserId = User.objects.latest('id').id
		vhn = "VHN"+str(100000+lastUserId+1)
		try:
			try:
				PvUser.objects.get(mobile_number = mobile_number)
				messages.warning(request,"User already registered with this Mobile Number.")
				return render(request, 'register.html')
#					response['status'] = 1
#					return JsonResponse(response) #User already registered with this mobile number
			except:
				print("code base 1")
				#print(sendSms('+91'+str(mobile_number),"Thanks for registering at vyala.Your unique VHN Number is "+vhn+". Use OTP "+activationToken+" to activate your account.OTP is valid for 3 minutes."))				

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
		mobile_number=mobile_number,activationToken = activationToken,user = user,pTime = datetime.utcnow().replace(tzinfo = utc))

		# if email:
		# 	try:
		# 		subject = "Welcome To Vyala Family"
		# 		body = "You have successfully registered at vyala and Your VHN Number is "+ vhn
		# 		sendEmail(email,subject,body)
		# 	except:
		# 		messages.warning('connection problem or invalid email!!')
		# 		return render(request,'register.html')	
		return render(request,'is_OTPvalid.html',{'vhn' : vhn})
#			response['status'] = 2 #OTP sent successfully and redirected to otp validation page
#			return JsonResponse(response)
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
			# sendSms("+91"+str(pvUser.mobile_number),"Thanks for registering at vyala.Your unique VHN Number is "+str(form['vhn'])+". Use OTP "+activationToken+" to activate you account.OTP is valid for 3 minutes.")
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
			# if not pvUser.otpValidTime(3):
			# 	messages.warning(request,"Plese resend OTP, OTP is expired now.")
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
					# sendSms(mobileNumber,"Your Vyala OTP to set password is: "+activationToken)
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
			# if not pvUser.otpValidTime(3):
			# 	messages.warning(request,"Plese resend OTP, OTP is expired now.")
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
					# sendSms(mobileNumber,"Use OTP: "+activationToken + "to activate your account.")
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
		return render(request,'login.html')
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

# @login_required(login_url = "/login/")
def profile(request):
	response = {}
	username = None
	i = 0
	d={}
	if request.method == 'POST':
		relative_names = None
		relations = None
		relative_vhnNumbers = None
		medical_history = None
		# username = request.user.username
		# user = User.objects.get(username = username)
		# pvUser = user.pvuser
		form = request.POST
		print(form)
		# country = form['country']
		# state = form['state']
		# city = form['city']
		# gender = form['gender']
		# relative_names = form.getlist('relative-name')
		# print(relative_names) 
		# relations = form.getlist('relation')
		# print(relations)
		# relative_vhnNumbers = form.getlist('relative-vhnNumber')
		# print(relative_vhnNumbers)
		# medical_history = form.getlist('medicalHistory')
		# print(medical_history)
		surgical_history = form.getlist('surgicalHistory')
		print(surgical_history)
		# try:
		# 	d["{0}".format(country)] = CountryMaster.objects.get(name = country)
		# except:	
		# 	print(country)
		# 	d["{0}".format(country)] = CountryMaster(name = form['country'], activeYesNo = True, lastModifiedDateTime = timezone.now())
		# 	d["{0}".format(country)].save()
		# try:
		# 	d["{0}".format(state)] = StateMaster.objects.get(name = state)
		# except:	
		# 	print(state)
		# 	d["{0}".format(state)] = StateMaster(name = form['state'], activeYesNo = True, lastModifiedDateTime = timezone.now(), country = d["{0}".format(country)])	
		# 	d["{0}".format(state)].save()
		# try:
		# 	d["{0}".format(city)] = CityMaster.objects.get(name = city)
		# except:	
		# 	print(city)
		# 	d["{0}".format(city)] = CityMaster(name = form['state'], activeYesNo = True, lastModifiedDateTime = timezone.now(), state = d["{0}".format(state)])
		# 	d["{0}".format(city)].save()
		# try:
		# 	d["{0}".format(gender)] = GenderMaster.objects.get(name = gender)
		# except:
		# 	print(gender)
		# 	d["{0}".format(gender)] = GenderMaster(name = form['gender'], activeYesNo = True, lastModifiedDateTime = timezone.now())
		# 	d["{0}".format(gender)].save()
		# for relation in relations:
		# 	try:
		# 		d["{0}".format(relation)] = RelationshipMaster.objects.get(name = relation)
		# 	except:
		# 		print(relation)	
		# 		d["{0}".format(relation)] = RelationshipMaster(name = relation, activeYesNo = True, lastModifiedDateTime = timezone.now())
		# 		d["{0}".format(relation)].save()
		# for medhistory in medical_history:
		# 	try:
		# 		d["{0}".format(medhistory)] = MedicalhistoryMaster.objects.get(name = medhistory)
		# 	except:
		# 		print(medhistory)	
		# 		d["{0}".format(medhistory)] = MedicalhistoryMaster(name = medhistory, activeYesNo = False, lastModifiedDateTime = timezone.now())
		# 		d["{0}".format(medhistory)].save()
		for surhistory in surgical_history:
			try:
				d["{0}".format(surhistory)] = SurgicalhistoryMaster.objects.get(name = surhistory)
			except:
				print(surhistory)	
				d["{0}".format(surhistory)] = SurgicalhistoryMaster(name = surhistory, activeYesNo =False, lastModifiedDateTime = timezone.now())
				d["{0}".format(surhistory)].save()
		
		# 			
		# pvProfile = PvProfile.objects.get_or_create(
		# 	# userId = pvUser,
		# 	countryId = d["{0}".format(country)],
		# 	stateId = d["{0}".format(state)],
		# 	cityId = d["{0}".format(city)],
		# 	# profilePhoto = request.FILES['profilePic'],
		# 	address = form['address'],
		# 	dob = form['DOB'],
		# 	gender = d["{0}".format(gender)],
		# 	lastModifiedDateTime = timezone.now(),
		# 	)
		
		# for relative in relative_names:
		# 	pvFamilyRelationship = PvFamilyRelationship.objects.get_or_create(
		# 		# patientId = pvUser,
		# 		relativeName = relative,
		# 		relationshipId = d["{0}".format(relations[i])],
		# 		# relative = User.objects.get(relative_vhnNumbers[i]).pvuser,
		# 		lastModifiedDateTime = timezone.now())
		# 	i += 1
		
		# pvSocialHistory = PvSocialHistory.objects.get_or_create(
		# 	paatientId = pvUser,
		# 	alcoholUsage = form['acheck'],
		# 	drinksPerWeek = form['drinks/week'],
		# 	tobacoUsage = form['tcheck'],
		# 	tobacoQuitDate = form['whenTobacoLeft'],
		# 	drugUsage = form['dcheck'],
		# 	drugQuitDate = form['whenDrugLeft'],
		# 	drugDetails = form['drugDetails'])

		# for medhistory in medical_history:
		# 	pvMedicalHistory = PvMedicalHistory.objects.get_or_create(
		# 		# patientId = pvUser,
		# 		mediacalHistoryId = d["{0}".format(medical_history)],
		# 		lastModifiedDateTime = timezone.now())

		for surhistory in surgical_history:
			pvSurgicalHistory = PvSurgicalHistory.objects.get_or_create(
				# patientId = pvUser,
				surgicalhistoryId = d["{0}".format(surhistory)],
				lastModifiedDateTime = timezone.now())

		messages.success(request,'saved')
		return render(request,'profile.html')
		# response['status'] = 1
		# return JsonResponse(response)
	else:
		return render(request,'profile.html')
	

# @login_required(login_url = "/login/")
# def relationship(request):
# 	response = {}
# 	if request.method == 'POST':
# 		pvUser = request.user.pvuser
# 		form = request.POST
# 		try:
# 			relative = User.objects.get(username = form['relVhnNo']).pvuser
# 		except:
# 			response['status'] = 2
# 			response['error'] = "Invalid VHN No. Of Relative"
# 			return JsonResponse(response)
# 		if not isinstance(form['relationship'],RelationshipMaster):
# 			form['relationship'] = RelationshipMaster(name = form['relationship'], activeYesNo = True, lastModifiedDateTime = datetime.now())
# 		pvRelationship = PvFamilyRelationship.objects.get_or_create(
# 		paatientId = pvUser,
# 		relativeName = form['name'],
# 		relationshipId = form['relationship'],
# 		relative = relative,
# 		lastModifiedDateTime = datetime.now())					
# 		response['status'] = 1
# 		return JsonResponse(response)
# 	else:
# 		response['status'] = 0
# 		response['error'] = 'Invalid Request !!'
# 		return JsonResponse(response)

# @login_required(login_url = "/login/")
# def deleteFamilyMember(request):
# 	response = {}
# 	if request.method == 'POST':
# 		pvUser = request.user.pvuser
# 		form = request.POST
# 		try:
# 			relative = User.objects.get(username = form['relVhnNo']).pvuser
# 		except:
# 			response['status'] = 0
# 			response['error0'] = "Invalid VHN No. Of Relative"
# 			return JsonResponse(response)
# 		try:
# 			pvRelationship = PvFamilyRelationship.objects.get(relative = relative)
# 			pvRelationship.delete()
# 			response['status'] = 1
# 		except:
# 			response['status'] = 2
# 			response['error2'] = "Not your family member"
# 		return JsonResponse(response)	
# 	else:
# 		response['status'] = 0
# 		response['error'] = 'Invalid Request !!'
# 		return JsonResponse(response)

# def medicalHistory(request):
# 	username = None
# 	if request.user.is_authenticated():
# 		username = request.user.username
# 		if request.method == 'POST':
# 			user = User.objects.get(username = username)
# 			pvUser = user.pvuser
# 			form = request.POST
# 			if not isinstance(form['medicalHistory'],MedicalhistoryMaster):
# 				form['medicalHistory'] = MedicalhistoryMaster(name = form['medicalHistory'], activeYesNo = True, lastModifiedDateTime = datetime.now())
# 			pvRelationship = PvFamilyRelationship.objects.get_or_create(
# 			paatientId = pvUser,
# 			medicalHistoryId = form['medicalHistory'],
# 			sharedYesNo = form['isShared'],
# 			activeYesNo = form['isActive'],
# 			lastModifiedDateTime = datetime.now())					

# 	else:
# 		return redirect('/login/')

# def SurgicalHistory(request):
# 	username = None
# 	if request.user.is_authenticated():
# 		username = request.user.username
# 		if request.method == 'POST':
# 			user = User.objects.get(username = username)
# 			pvUser = user.pvuser
# 			form = request.POST
# 			if not isinstance(form['surgicalHistory'],SurgicalhistoryMaster):
# 				form['surgicalHistory'] = SurgicalhistoryMaster(name = form['surgicalHistory'], activeYesNo = True, lastModifiedDateTime = datetime.now())
# 			pvRelationship = PvFamilyRelationship.objects.get_or_create(
# 			paatientId = pvUser,
# 			surgicalHistoryId = form['surgicalHistory'],
# 			sharedYesNo = form['isShared'],
# 			activeYesNo = form['isActive'],
# 			lastModifiedDateTime = datetime.now())					

# 	else:
# 		return redirect('/login/')	
'''
def SocialHistory(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
		if request.method == 'POST':
			user = User.objects.get(username = username)
			pvUser = user.pvuser
			form = request.POST
			if not isinstance(form['surgicalHistory'],SurgicalhistoryMaster):
				form['surgicalHistory'] = SurgicalhistoryMaster(name = form['surgicalHistory'], activeYesNo = True, lastModifiedDateTime = datetime.now())
			pvRelationship = PvFamilyRelationship.objects.get_or_create(
			paatientId = pvUser,
			alcoholUsage = form['alcoholUsage'],
			drinksPerWeek = form['drinks/week'],
			tobacoUsage = form['tobacoUsage'],
			tobacoQuitDate = form['whenTobacoLeft'],
			drugUsage = form['drugsUsage'],
			drugQuitDate = form['whenDrugLeft'],
			drugDetails = form['drugDetails'])					

	else:
		return redirect('/login/')			

'''

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
	return render(request,'profile.html')