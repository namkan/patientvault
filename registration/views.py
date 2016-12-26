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
			mobile_number = form.cleaned_data["mobile_number"]
			password = form.cleaned_data["password"]
			user = PvUser.objects.get_or_create(
				email=email,
				mobile_number=mobile_number,)

			user = User.objects.create_user(
				username=first_name+'123',
				first_name=first_name,
				last_name=last_name,
				password=password,)

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