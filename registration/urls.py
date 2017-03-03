from django.conf.urls import url, include, patterns
from registration.views import *
from django.conf import settings
urlpatterns = [
	url(r'^login/',signIn, name='login view'),
    url(r'^register/',register, name='registeration view'),
    url(r'^OTPvalidation/',OTPvalidation, name='registeration view'),
    url(r'^resendOTP/',resendOTP,name='resend OTP'),
    url(r'^FindAccount/',FindAccount,name='user finds his account to set password'),
    url(r'^SetPassword/(?P<pvUser>[\w\-]+)/$',SetPassword,name='set password'),
    url(r'^changePass/',changePass,name='change password'),
    url(r'^completeprofile/',profile,name='complete your profile'),
    url(r'^relTest/',relation,name='rel'),
    url(r'^ActivateAccount/',ActivateAccount,name='for activation of account'),
    url(r'^checkrelation/',checkRelation,name='check'),
    # url(r'^deleteMember/',deleteFamilyMember,name='rel'),
    url(r'^logout/',logout_view,name='logout the user'),
    ]
