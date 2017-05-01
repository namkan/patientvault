from django.conf.urls import url, include, patterns
from ephr_module.views import *
from django.conf import settings
urlpatterns = [
	url(r'^upload/',uploadDocuments, name='document uploading'),
	url(r'^documentShareStatus/',changeDocumentShareStatus, name='changes sharable status'),
	url(r'^radioShareStatus/',changeRadioShareStatus, name='changes sharable status'),
	url(r'^labShareStatus/',changeLabShareStatus, name='changes sharable status'),
	url(r'^medicationShareStatus/',changeMedicationShareStatus, name='changes sharable status'),
	url(r'^checkReportName/',checkReportName, name='validates report name'),
	url(r'^labreport/',labview, name='changes sharable status'),
	url(r'^radioreport/',radioview, name='changes sharable status'),
	url(r'^allergies/',allergies,name='allergy_portal'),
	url(r'^medication/',medication,name='medication_portal'),
	url(r'^reminders/',reminder,name='medication_portal'),
	url(r'^visits/',visit,name='medication_portal'),
	url(r'^diagnosis/',diagnosis,name='medication_portal'),
	url(r'^personalinfo/',personalInfo,name='shows personal information of user'),
	url(r'^allergyupdate/',allergy_update,name='allergy_update'),
	url(r'^allergydelete/',allergy_delete,name='allergy_delete'),
	url(r'^coversheet/',coversheet,name='coversheet_'),
	url(r'^coversheet1/',coversheet1,name='coversheet_1'),
	url(r'^coversheet2/',coversheet2,name='coversheet_2'),
	url(r'^coversheetupdate/',coversheeet_update, name='coversheet'),
	url(r'^coversheetdelete/',coversheeet_delete, name='coversheet_delete'),
	url(r'^coversheetupdate1/',coversheet_update1,name='coversheet1'),
	url(r'^coversheetdelete1/',coversheeet_delete1, name='coversheet_delete1'),
	url(r'^coversheetupdate2/',coversheet_update2,name='coversheet2'),
	url(r'^coversheetdelete2/',coversheet_delete2, name='coversheet_delete2'),
	url(r'^coversheetupdate3/',coversheet_update3, name='socialsheet'),
	url(r'^dashboard/',show_dashboard, name='dashboard'),
	url(r'^historyShareStatus/',changeHistoryShareStatus, name='dashboard'),
    ]