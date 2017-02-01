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
from .forms import RegistrationForm,LoginForm
from django.http import HttpResponse,HttpResponseRedirect
from random import randint
import requests
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core import mail
from datetime import datetime
COMPANY_NUMBER = "+16024973298"

def contextCall(request):
	pass

#view for login page
def signIn(request):
	if request.method == 'POST':
		form1 = LoginForm(request.POST or None)
		form = RegistrationForm()
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			try:
				username = User.objects.get(username = username)
			except:	
				try:
					username = PvUser.objects.get(mobile_number = username).user.username
				except:
					messages.warning(request,'Invalid Credentials!!')
					return render(request,'login.html',{'form1':form})		
			try:
				user = authenticate(username = username, password = password)
				if user is not None:
		    	# the password verified for the user
					if user.is_active:
						login(request,user)
						return render(request,'dashboard.html')	
					else:
						messages.warning(request,"The password is valid, but the account has been disabled!")
				else:
					messages.warning(request,"Invalid Credentials !!!")
	#			user = User.objects.get(username=form['username'],password=form['password'])
	#			print("user is found")
				return render(request,'login.html',{'form1':form1,'form':form})
					
			except:
				print("user is not found,please create account!!")	
				return render(request,'login.html',{'form1':form1,'form':form})
	else:		
		form1 = LoginForm()
		form = RegistrationForm()
		return render(request,'login.html',{'form1':form1,'form':form})


@csrf_exempt
#View for registration page
def register(request):
	response = {}
	if request.method == 'POST':
		form = RegistrationForm(request.POST or None)
		if form.is_valid():
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			email = form.cleaned_data["email"]
			mobile_number = str(form.cleaned_data["mobile_number"])
			password = form.cleaned_data["password"]
			activationToken = str(randomWithNDigits(8))
			lastUserId = User.objects.latest('id').id
			vhn = "VHN"+str(100000+lastUserId+1)
			try:
				try:
					PvUser.objects.get(mobile_number = mobile_number)
					messages.warning(request,"User already registered with Mobile Number.")
					return render(request, 'login.html',{'form':form})
#					response['status'] = 1
#					return JsonResponse(response) #User already registered with this mobile number
				except:
					print("code base 1")
					if sendSms('+91'+str(mobile_number),"Thanks for registering at vyala.Your unique VHN Number is "+vhn+". Use OTP "+activationToken+" to activate you account.") == 'failure':
						messages.warning(request,"Connection problem or Invalid Phone Number !!!")
						return render(request, 'login.html',{'form':form})
			except:
				print("code base 2")
				messages.warning(request,"Connection problem or Invalid Phone Number !!!")
				return render(request, 'login.html',{'form':form})
#				response['status'] = 0
#				return JsonResponse(response) #connection problem or invalid phone number
			user = User.objects.create_user(
				username=vhn,
				first_name=first_name,
				last_name=last_name,
				password=password,)
			pvUser = PvUser.objects.get_or_create(
			email=email,
			mobile_number=mobile_number,activationToken = activationToken,user = user)

			if email:
				subject = "Welcome To Vyala Family"
				body = "You have successfully registered at vyala and Your VHN Number is "+ vhn
				sendEmail(email,subject,body)

			return render(request,'is_OTPvalid.html',{'vhn' : vhn})
#			response['status'] = 2 #OTP sent successfully and redirected to otp validation page
#			return JsonResponse(response)
	else:
		form = RegistrationForm()
        
	return redirect('/login/')

#View for OTP validation
@csrf_exempt
def OTPvalidation(request):
	if request.method == 'POST':
		form = request.POST
		try:
			user = User.objects.get(username = form['vhn'])
			pvUser = user.pvuser
		except:
			return HttpResponse("Forbidden!!!")
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
			pvUser.save()
			messages.warning(request,'Please enter correct OTP !!')
			return render(request,'is_OTPvalid.html')	
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
			sendSms("+91"+str(pvUser.mobile_number),"Thanks for registering at vyala.Your unique VHN Number is "+str(form['vhn'])+". Use OTP "+activationToken+" to activate you account.")
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
def FindAccount(request):
	response={}
	if request.method == 'POST':
		form = request.POST
		activationToken = str(randomWithNDigits(8))
		try:
			user = User.objects.get(username = form['VHN'])
			pvUser = user.pvuser
			if form['OTP']:
				if form['OTP'] == pvUser.activationToken:
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
					sendSms(mobileNumber,"Your Vyala OTP : "+activationToken)
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

#view to reset password	
@login_required(login_url = "/login")	
def SetPassword(request,pvUser):
	response = {}
	if request.method == 'POST':
		form = request.POST
		pv = User.objects.get(username = form['vhn'])
		pv.set_password(form['password'])
		pv.save()
		return HttpResponse('Password is successfully changed')
	else:
		return render(request,'SetPassword.html',{"vhn":pvUser})	

#view for changing passsword
@csrf_exempt
@login_required(login_url = "/login")
def changePass(request):
	response={}
	username = None
	if request.user.is_authenticated():
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
						response['status'] = 5 # now show new Password button
						return JsonResponse(response)
				else:
					response['status']=2 # wrong currentPass8
					return JsonResponse(response)				

		else:
			print(1)
			response['status']=1
			return JsonResponse(response)	
	else:
		response['status']=4
		return JsonResponse(response)	

@login_required(login_url = "/login/")
def profile(request):
	response = {}
	username = None
	if request.method == 'POST':
		username = request.user.username
		user = User.objects.get(username = username)
		pvUser = user.pvuser
		form = request.POST
		if not isinstance(form['country'],CountryMaster):
			form['country'] = CountryMaster(name = form['country'], activeYesNo = True, lastModifiedDateTime = datetime.now())
		if not isinstance(form['state'],StateMaster):
			form['state'] = StateMaster(name = form['state'], activeYesNo = True, lastModifiedDateTime = datetime.now(), country = form['country'])
		if not isinstance(form['city'],CityMaster):
			form['city'] = CityMaster(name = form['city'], activeYesNo = True, lastModifiedDateTime = datetime.now(), state = form['state'])
		if not isinstance(form['medicalHistory'],MedicalhistoryMaster):
				form['medicalHistory'] = MedicalhistoryMaster(name = form['medicalHistory'], activeYesNo = True, lastModifiedDateTime = datetime.now())
		if not isinstance(form['surgicalHistory'],SurgicalhistoryMaster):
				form['surgicalHistory'] = SurgicalhistoryMaster(name = form['surgicalHistory'], activeYesNo = True, lastModifiedDateTime = datetime.now())	
		pvProfile = PvProfile.objects.get_or_create(
			userId = pvUser,
			country = form['country'],
			state = form['state'],
			city = form['city'],
			profilePhoto = request.FILES['profilePic'],
			address = form['address'],
			dob = form['DOB'],
			)
		PvSocialHistory = PvSocialHistory.objects.get_or_create(
			paatientId = pvUser,
			alcoholUsage = form['acheck'],
			drinksPerWeek = form['drinks/week'],
			tobacoUsage = form['tcheck'],
			tobacoQuitDate = form['whenTobacoLeft'],
			drugUsage = form['dcheck'],
			drugQuitDate = form['whenDrugLeft'],
			drugDetails = form['drugDetails'])

		response['status'] = 1
		return JsonResponse(response)
	else:
		return render(request,'profile.html')
	

@login_required(login_url = "/login/")
def relationship(request):
	response = {}
	if request.method == 'POST':
		pvUser = request.user.pvuser
		form = request.POST
		try:
			relative = User.objects.get(username = form['relVhnNo']).pvuser
		except:
			response['status'] = 2
			response['error'] = "Invalid VHN No. Of Relative"
			return JsonResponse(response)
		if not isinstance(form['relationship'],RelationshipMaster):
			form['relationship'] = RelationshipMaster(name = form['relationship'], activeYesNo = True, lastModifiedDateTime = datetime.now())
		pvRelationship = PvFamilyRelationship.objects.get_or_create(
		paatientId = pvUser,
		relativeName = form['name'],
		relationshipId = form['relationship'],
		relative = relative,
		lastModifiedDateTime = datetime.now())					
		response['status'] = 1
		return JsonResponse(response)
	else:
		response['status'] = 0
		response['error'] = 'Invalid Request !!'
		return JsonResponse(response)

@login_required(login_url = "/login/")
def deleteFamilyMember(request):
	response = {}
	if request.method == 'POST':
		pvUser = request.user.pvuser
		form = request.POST
		try:
			relative = User.objects.get(username = form['relVhnNo']).pvuser
		except:
			response['status'] = 0
			response['error0'] = "Invalid VHN No. Of Relative"
			return JsonResponse(response)
		try:
			pvRelationship = PvFamilyRelationship.objects.get(relative = relative)
			pvRelationship.delete()
			response['status'] = 1
		except:
			response['status'] = 2
			response['error2'] = "Not your family member"
		return JsonResponse(response)	
	else:
		response['status'] = 0
		response['error'] = 'Invalid Request !!'
		return JsonResponse(response)

def medicalHistory(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
		if request.method == 'POST':
			user = User.objects.get(username = username)
			pvUser = user.pvuser
			form = request.POST
			if not isinstance(form['medicalHistory'],MedicalhistoryMaster):
				form['medicalHistory'] = MedicalhistoryMaster(name = form['medicalHistory'], activeYesNo = True, lastModifiedDateTime = datetime.now())
			pvRelationship = PvFamilyRelationship.objects.get_or_create(
			paatientId = pvUser,
			medicalHistoryId = form['medicalHistory'],
			sharedYesNo = form['isShared'],
			activeYesNo = form['isActive'],
			lastModifiedDateTime = datetime.now())					

	else:
		return redirect('/login/')

def SurgicalHistory(request):
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
			surgicalHistoryId = form['surgicalHistory'],
			sharedYesNo = form['isShared'],
			activeYesNo = form['isActive'],
			lastModifiedDateTime = datetime.now())					

	else:
		return redirect('/login/')	
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
	print(data)
	return(data['status'])

#function for generating activationToken
def randomWithNDigits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)

def relation(request):
	return render(request,'profile.html')