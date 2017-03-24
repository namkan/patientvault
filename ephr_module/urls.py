from django.conf.urls import url, include, patterns
from ephr_module.views import *
from django.conf import settings
urlpatterns = [
	url(r'^upload/',uploadDocuments, name='document uploading'),
	url(r'^changeShareStatus/',changeDocumentShareStatus, name='changes sharable status'),
	url(r'^labreport/',labview, name='changes sharable status'),
	url(r'^radioreport/',radioview, name='changes sharable status'),
	url(r'^allergies/',allergies,name='allergy_portal'),
	url(r'^medication/',medication,name='medication_portal'),
    ]