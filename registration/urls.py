from django.conf.urls import url, include, patterns
from registration.views import *
from django.conf import settings
urlpatterns = [
    url(r'^register/',register, name='registeration view'),
    ]