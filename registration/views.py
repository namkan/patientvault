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

def contextCall(request):
	pass

def register(request):

	if request.method == 'POST':
	#print(request.POST["first_name"])
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
					sendSms(mobile_number,"+16024973298","Your Vyala OTP : "+activationToken)
			except:
				print("code base 2")
				messages.warning(request,"Invalid Phone Number !!!")
				return render(request, 'login.html',{'form':form})
			user = PvUser.objects.get_or_create(
				email=email,
				mobile_number=mobile_number,activationToken = activationToken)

			lastUserId = User.objects.latest('id').id
			vhn = "VHN"+str(100000+lastUserId+1)
			user = User.objects.create_user(
				username=vhn,
				first_name=first_name,
				last_name=last_name,
				password=password,)
			if email:
				subject = "Welcome To Vyala Family"
				body = "You have successfully registered at vyala"
				sendEmail(email,subject,body)

			return HttpResponse('thanks')
	
	#saved = False
    #if request.method == "POST":
        #Get the posted form
    #    RegForm = PvUser(request.POST, request.FILES)
    #    if RegForm.is_valid():
    #        userInfo = PvUser()
    #        userInfo.name = RegForm.cleaned_data["name"]
    #        userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
    #        userInfo.email = RegForm.cleaned_data["email"]
    #        userInfo.password = RegForm.cleaned_data["password"]
    #        userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
    #        userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
    #        userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
    #        userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
    #        userInfo.save()
    #        saved = True'''
	else:
		form = RegistrationForm()
        
	return render(request, 'login.html',{'form':form})



def sendEmail(recipient, subject, body):

	return requests.post(
		"https://api.mailgun.net/v3/mg.technex.in/messages",
		auth=("api", "key-cf7f06e72c36031b0097128c90ee896a"),
		data={"from": "Suppor VyalaTech <rishabh.vyala@gmail.com>",
			"to": recipient,
			"subject": subject,
			"text": body})


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
