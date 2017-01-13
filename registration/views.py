from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PvUser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import RegistrationForm
from django.http import HttpResponse,HttpResponseRedirect
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
		print(form['username'])
		try:
			username = User.objects.get(username = form['username'])
		except:	
			try:
				username = PvUser.objects.get(mobile_number = form['username']).user.username
			except:
				messages.warning(request,'Invalid Credentials!!')
				return render(request,'login.html')		
		try:
			user = authenticate(username=username, password=form['password'])
			print(user)
			if user is not None:
	    	# the password verified for the user
				if user.is_active:
					messages.success(request,"User is valid, active and authenticated")
					print('1')	
				else:
					messages.warning(request,"The password is valid, but the account has been disabled!")
					print('2')
#			user = User.objects.get(username=form['username'],password=form['password'])
#			print("user is found")
			return render(request,'login.html')
				
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
			mobile_number = str(form.cleaned_data["mobile_number"])
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
					sendSms('+91'+str(mobile_number),COMPANY_NUMBER,"Your Vyala OTP : "+activationToken)
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

#view for finding account and sending otp on registered mobile number
def FindAccount(request):
	response={}
	if request.method == 'POST':
		form = request.POST
		activationToken = str(randomWithNDigits(8))
		if 1:
			user = User.objects.get(username = form['VHN'])
			pvUser = user.pvuser
			print(form['OTP'])
			if form['OTP']:
				print(1)
				if form['OTP'] == pvUser.activationToken:
					response['status'] = 5 
					response['vhn'] = form['VHN']
					return JsonResponse(response)
				else:
					response['status']=3
					return jsonResponse(response)
			else:
				print(2)		
				if 1:
					mobileNumber = "+91"+str(pvUser.mobile_number) 
					print(mobileNumber)
					sendSms(mobileNumber,"Your Vyala OTP : "+activationToken)
					pvUser.activationToken = activationToken
					pvUser.save()
					response['status'] = 1 
					return JsonResponse(response)
				else:
					response['status'] = 0 ### connection error or unknown error
					return JsonResponse(response)				
		else:
			response['status'] = 2 # INvalid VHN Number
			return JsonResponse(response)
		
	else:
		return render(request,'FindAccount.html')		

#view for changing password		
def SetPassword(request,pvUser):
	response = {}
	if request.method == 'POST':
		form = request.POST
		pv = User.objects.get(username = pvUser).pvuser
		pv.user.password = form['password']
		pv.save()
		response['status']=1
		return jsonResponse(response)
	else:
		return render(request,'SetPassword.html')	





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
			sendSms("+91"+str(pvUser.mobile_number),COMPANY_NUMBER,"Your Vyala OTP : "+activationToken)
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

	print(data['status'])

#function for generating activationToken
def randomWithNDigits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)
