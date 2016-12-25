from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *#user_info,quiz,options,questions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def contextCall(request):
	pass

def register(request):
	'''
	saved = False
    if request.method == "POST":
        #Get the posted form
        RegForm = PvUser(request.POST, request.FILES)
        if RegForm.is_valid():
            userInfo = PvUser()
            userInfo.name = RegForm.cleaned_data["name"]
            userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
            userInfo.email = RegForm.cleaned_data["email"]
            userInfo.password = RegForm.cleaned_data["password"]
            userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
            userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
            userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
            userInfo.phoneNo = RegForm.cleaned_data["phoneNo"]
            userInfo.save()
            saved = True
        else:
            MyProfileForm = Profileform()
        return render(request, 'saved.html', locals())
    else:'''
	return render(request, 'login.html')