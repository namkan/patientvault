from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PvUser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import RegistrationForm
from django.http import HttpResponse
from random import randint
import requests
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core import mail
COMPANY_NUMBER = "+16024973298"

def contextCall(request):
	pass

#view for login page
def login(request):
	if request.method == 'POST':
		form = request.POST
		try:
			try:
				user = authenticate(username=form['username'], password=form['password'])
				print(user)
				if user is not None:
		    	# the password verified for the user
					if user.is_active:
						print("User is valid, active and authenticated")
						print('1')	
					else:
						messages.warning(request,"The password is valid, but the account has been disabled!")
						print('2')
	#			user = User.objects.get(username=form['username'],password=form['password'])
	#			print("user is found")
				return render(request,'login.html')
			except:
				pvuser = pvUser.objects.get(mobile_number = )	
		except:
			print("user is not found,please create account!!")	
			return render(request,'login.html')
	else:		
		return render(request,'login.html')



#View for registration page
def register(request):

	if request.method == 'POST':
		form = RegistrationForm(request.POST or None)
		if form.is_valid():
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			email = form.cleaned_data["email"]
			mobile_number = "+91"+str(form.cleaned_data["mobile_number"])
			password = form.cleaned_data["password"]
			activationToken = str(randomWithNDigits(8))

			try:
				try:
					PvUser.objects.get(mobile_number = mobile_number)
					messages.warning(request,"User already registered with Mobile Number.")
					return render(request,'login.html',{'form':form})
					print("code base 0")
				except:
					print("code base 1")
					sendSms(mobile_number,COMPANY_NUMBER,"Your Vyala OTP : "+activationToken)
			except:
				print("code base 2")
				messages.warning(request,"Invalid Phone Number !!!")
				return render(request, 'login.html',{'form':form})
			lastUserId = User.objects.latest('id').id
			vhn = "VHN"+str(100000+lastUserId+1)
			print(vhn)
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
				body = "You have successfully registered at vyala"
				sendEmail(email,subject,body)

			return render(request,'is_OTPvalid.html',{'vhn' : vhn})
	else:
		form = RegistrationForm()
        
	return render(request,'login.html',{'form':form})

#View for OTP validation
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
			return HttpResponse('Your Phone Number is verified and your account is activated')
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
		print(form['vhn'])
		try:
			user = User.objects.get(username = form['vhn'])
			pvUser = user.pvuser
		except:
			messages.warning(request,'Invalid VHN number')
			response['status'] = 2 # INvalid VHN Number
			return JsonResponse(response)
		if True:
			sendSms("+"+str(pvUser.mobile_number),COMPANY_NUMBER,"Your Vyala OTP : "+activationToken)
			pvUser.activationToken = activationToken
			pvUser.save()
			response['status'] = 1 
			return JsonResponse(response)
		else:
			response['status'] = 0 ### connection error or unknown error
			return JsonResponse(response)
	else:
		response['status'] = "Invalid!!"
		return JsonResponse(response)

#def sendEmail(recipient, subject, body):
#
#	return requests.post(
#		auth=("api", "key-cf7f06e72c36031b0097128c90ee896a"),
#		data={"from": "Support VyalaTech <rishabh.vyala@gmail.com>",
#			"to": recipient,
#			"subject": subject,
#			"text": body})

def sendEmail(recipient, subject, body):
	print(recipient)
	email = EmailMessage(
		subject=subject,
		body=body,
		from_email='naman.kansal@vyalatech.com',
		to=['recipient'],
    )
	email.send()


def sendSms(recipientNumber, fromNumber, content):
	from twilio.rest import TwilioRestClient
	account_sid = "AC661f41359fe195c99b7b774bc3599e11"
	auth_token = "a4135c97cf57d726fc12024f8782c381"
	client = TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(to=recipientNumber, from_=fromNumber,body=content)

def randomWithNDigits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)
