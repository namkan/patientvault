from django.conf.urls import url, include, patterns
from ephr_module.views import *
from django.conf import settings
urlpatterns = [
	url(r'^upload/',uploadDocuments, name='document uploading'),
    ]