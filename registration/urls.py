from django.conf.urls import url, include, patterns
from registration.views import *
from django.conf import settings
urlpatterns = [
	url(r'^login/',login, name='login view'),
    url(r'^register/',register, name='registeration view'),
    url(r'^OTPvalidation/',OTPvalidation, name='registeration view'),
    url(r'^resendOTP/',resendOTP,name='resend OTP'),
    ]
