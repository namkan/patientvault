from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
import cloudinary,cloudinary.uploader,cloudinary.api
from .models import *
from registration.models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash
import mimetypes
# Create your views here.

@login_required(login_url='/login/')
def uploadDocuments(request):
	pvUser = request.user.pvuser
	reports = PvUploadedFiles.objects.filter(last_modified_by=pvUser)
	if request.method == "POST":
		info_dic = None
		data = request.POST
		print(request.FILES['report'].name)
		tup = mimetypes.guess_type(request.FILES['report'].name)
		if tup[0] == 'image/jpeg' or tup[0] == 'image/png':
			info_dic = cloudinary.uploader.upload(request.FILES['report'])
			reports = PvUploadedFiles.objects.get_or_create(
				filename = data['Report Name'],
				file_type = data['Report Type'],
				file_url = info_dic['secure_url'],
				added_on = datetime.now().date(),
				checkbox_id = data['Report Name'].replace(' ', '_'),
				last_modified_by = pvUser
				)
			return render(request,'upload_reports.html',{'reports':reports,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})
		else:
			messages.warning(request,'NOT VALID FORMATE OF IMAGE!!')
			return render(request,'upload_reports.html',{'reports':reports,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})
	else:
		return render(request,'upload_reports.html',{'reports':reports,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

@csrf_exempt
@login_required(login_url='/login')
def changeDocumentShareStatus(request):
	response = {}
	pvUser = request.user.pvuser
	if request.method == 'POST':
		data = request.POST
		print(data)
		desired_model = PvUploadedFiles.objects.get(id=data['id'], last_modified_by=pvUser)
		desired_model.is_sharable = bool(int(data['shareStatus']))
		desired_model.save()
		response['status'] = 1
		return JsonResponse(response)
	else:
		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def changeRadioShareStatus(request):
	response = {}
	pvUser = request.user.pvuser
	if request.method == 'POST':
		data = request.POST
		print(data)
		desired_model = PvRadorders.objects.get(id=data['id'], patient_id=pvUser)
		desired_model.is_sharable = bool(int(data['shareStatus']))
		desired_model.save()
		response['status'] = 1
		return JsonResponse(response)
	else:
		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login/')
def changeMedicationShareStatus(request):
	response = {}
	pvUser = request.user.pvuser
	if request.method == 'POST':
		data = request.POST
		print(data)
		desired_model = PvPrescription.objects.get(id=data['id'], patient_id=pvUser)
		desired_model.is_sharable = bool(int(data['shareStatus']))
		desired_model.save()
		response['status'] = 1
		return JsonResponse(response)
	else:
		return HttpResponse('403 bad request')		

@csrf_exempt
@login_required(login_url='/login/')
def changeLabShareStatus(request):
	response = {}
	pvUser = request.user.pvuser
	if request.method == 'POST':
		data = request.POST
		print(data)
		desired_model = PvLaborders.objects.get(id=data['id'], patient_id=pvUser)
		desired_model.is_sharable = bool(int(data['shareStatus']))
		desired_model.save()
		response['status'] = 1
		return JsonResponse(response)
	else:
		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login/')
def changeHistoryShareStatus(request):
	response = {}
	print(0)
	if request.method == 'POST':
		print(1)
		data = request.POST
		print(data)
		pvUser = PvUser.objects.get(id=data['id'])
		if data['class'] == 'js-switch social':
			pvUser.shareSocial = bool(int(data['shareStatus']))
		if data['class'] == 'js-switch medical':
			pvUser.shareMedical = bool(int(data['shareStatus']))
		if data['class'] == 'js-switch surgical':
			pvUser.shareSurgical = bool(int(data['shareStatus']))
		if data['class'] == 'js-switch family':
			pvUser.shareFamily = bool(int(data['shareStatus']))
		pvUser.save()
		response['status'] = 1
		return JsonResponse(response)
	else:
		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def checkReportName(request):
	response = {}
	pvUser = request.user.pvuser
	if request.method == 'POST':
		data = request.POST
		print(data)
		try:
			desired_model = PvUploadedFiles.objects.get(filename=data['name'], last_modified_by=pvUser)
			print('try')
			response['status'] = 0
			return JsonResponse(response)
		except:
			print('except')
			response['status'] = 1
			print('ho gya')
			return JsonResponse(response)
	else:
		return HttpResponse('403 bad request')
			
@login_required(login_url='/login')			
def labview(request):
	pvUser = request.user.pvuser
	orders = PvLaborders.objects.filter(patient_id=pvUser)
	return render(request,'lab_reports.html',{'orders': orders,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

@login_required(login_url='/login')
def radioview(request):
	pvUser = request.user.pvuser
	orders = PvRadorders.objects.filter(patient_id=pvUser)
	radios = PvUploadedFiles.objects.filter(last_modified_by=pvUser, file_type='Radiology Report')
	print(radios)
	return render(request,'radio_reports.html',{'orders': orders,'radios':radios,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

@login_required(login_url='/login')
def allergies(request):
	pvUser = request.user.pvuser
	categories = AllergyCategoryMaster.objects.all()
	effects = AllergyServerityMaster.objects.all()
	datas = PvAllergy.objects.filter(patient_id=pvUser)
	if request.method == 'POST':
		form = request.POST
		substance = form["substance"]
		reaction_details = form["reaction_details"]
		categoryOjbect = AllergyCategoryMaster.objects.get(name = form['category'])
		serverityObjects = AllergyServerityMaster.objects.get(name = form['effect'])
		pv_allergy = PvAllergy.objects.get_or_create(
		substance = substance,
		category_id = categoryOjbect,
		serverity_id = serverityObjects,
		reactions = reaction_details,
		active_yesno = True,
		patient_id = pvUser,
		last_modified_date_time = datetime.now()
			)
		return render(request,'allergies.html',{'categories':categories,'effects':effects,'datas':datas,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

	else:
		return render(request,'allergies.html',{'categories':categories,'effects':effects,'datas':datas,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

@csrf_exempt
@login_required(login_url='/login/')
def medication(request):
	pvUser = request.user.pvuser
	pvprescriptionDetails = PvPrescriptionDetails.objects.filter(patient_id=pvUser)
	pvPrescriptions = PvPrescription.objects.filter(patient_id=pvUser)
	return render(request,'medication.html',{'details' : pvprescriptionDetails,'details1' : pvPrescriptions,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

@login_required(login_url='/login/')
def visit(request):
	pvUser = request.user.pvuser
	visits = DpVisits.objects.filter(patient_id=pvUser)
	return render(request,'visit.html',{'visits':visits,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

@login_required(login_url='/login/')
def reminder(request):
	pvUser = request.user.pvuser
	reminders = PvReminders.objects.filter(patient_id=pvUser)
	date = datetime.now().date()
	return render(request,'reminder.html',{'reminders':reminders,'date':date,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

def diagnosis(request):
	pvUser = request.user.pvuser
	codes = Icd10.objects.all()
	modes = DiagnosisStatusMaster.objects.all()
	rodes = DpUser.objects.all()
	date = datetime.now().date()
	return render(request,'daignosis.html',{'info':zip(codes,modes,rodes),'date': date,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

def personalInfo(request):
	pvUser = request.user.pvuser
	pvProfile = PvProfile.objects.get(userId=pvUser)
	if request.method == 'POST':
		form = request.POST
		countryObjects = CountryMaster.objects.get(name = form['country'])
		stateObjects = StateMaster.objects.get(name = form['state'])
		cityObjects = CityMaster.objects.get(name = form['city'])
		address = form['address']
		genderObjects = GenderMaster.objects.get(name = form['genders'])

		personal1 = PvProfile.objects.get(id = form['mysocial'])

		personal1.gender = genderObjects
		personal1.countryId = countryObjects
		personal1.stateId = stateObjects
		personal1.cityId = cityObjects
		personal1.address = address
		pvUser.user.first_name = form['first_name']
		pvUser.user.last_name = form['last_name']
		personal1.save()
		pvUser.user.save()

		return render(request,'personal_info.html',{'pvuser':pvUser,'pvprofile':pvProfile,'url':get_gravatar_url(pvUser.email, size=150)})
	else:
		return render(request,'personal_info.html',{'pvuser':pvUser,'pvprofile':pvProfile,'url':get_gravatar_url(pvUser.email, size=150)})

@login_required(login_url='/login')
def allergy_update(request):
	pvUser = request.user.pvuser
	categories = AllergyCategoryMaster.objects.all()
	effects = AllergyServerityMaster.objects.all()
	datas = PvAllergy.objects.filter(patient_id=pvUser)

	if request.method == 'POST':
		form = request.POST
		
		allergyOjbect = AllergyCategoryMaster.objects.get(name = form['category1'])
		serverityObjects = AllergyServerityMaster.objects.get(name = form['serverity1'])
		
		info_allergy = PvAllergy.objects.get(substance = form['my_Id'])
		info_allergy.category_id = allergyOjbect
		info_allergy.serverity_id = serverityObjects
		info_allergy.last_modified_date_time = datetime.now()
		info_allergy.save()
		return redirect('/allergies/')
	else:

		return render(request,'allergies.html',{'categories':categories,'effects':effects,'datas':datas})

@login_required(login_url='/login')
def allergy_delete(request):
	pvUser = request.user.pvuser
	categories = AllergyCategoryMaster.objects.all()
	effects = AllergyServerityMaster.objects.all()
	datas = PvAllergy.objects.filter(patient_id=pvUser)

	if request.method == 'POST':
		form = request.POST
		info_allergy = PvAllergy.objects.get(substance= form['my_Id'])
		info_allergy.delete()
		return redirect('/allergies/')
	else:
		return HttpResponse('404 bad request')

@csrf_exempt
@login_required(login_url='/login/')
def coversheet(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)
	relations = RelationshipMaster.objects.all()
	if request.method == 'POST':
		form = request.POST
		categoryObject = MedicalhistoryMaster.objects.create(name = form['problem'])
		# surgeryObject = SurgicalhistoryMaster.objects.create(name = form['surgery'])
		# surgery_date = form["surgery_dates"]
		started_on = form["started"]
		current_status = form["status"]
		resolved_on = form["resolve"]

		info1 = PvMedicalHistory.objects.get_or_create(
		mediacalHistoryId = categoryObject,
		started_on = started_on,
		current_status = current_status,
		resolved_on = resolved_on,
		patientId = pvUser
			)

		# info2 = PvSurgicalHistory.objects.create(
		# surgicalhistoryId = surgeryObject,
		# surgery_date = surgery_date,
		# )


		return render(request,'coversheet.html',{'relations':relations,'socials':socials,'medicals':medicals,'surgeries':surgeries,'families':families,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})

	else:

		return render(request,'coversheet.html',{'relations':relations,'socials':socials,'medicals':medicals,'surgeries':surgeries,'families':families,'pvuser':pvUser,'url':get_gravatar_url(pvUser.email, size=150)})


@csrf_exempt
@login_required(login_url='/login')
def coversheet1(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)

	if request.method == 'POST':
		form = request.POST
		surgeryObject = SurgicalhistoryMaster.objects.get_or_create(name = form['surgery'])
		surgery_date = form["surgery_dates"]

		info2 = PvSurgicalHistory.objects.create(
		surgicalhistoryId = surgeryObject,
		surgery_date = surgery_date,
		patientId = pvUser
			)


		return redirect('/coversheet/')
	else:

		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login/')
def coversheet2(request):
	pvUser = request.user.pvuser
	if request.method == 'POST':
		form = request.POST
		familyObject = FamilyhistoryMaster.objects.get_or_create(name = form['family'])
		relationObject = RelationshipMaster.objects.get_or_create(name = form['relationship'])

		info2 = PvFamilyHistory.objects.create(
		familyhistoryId = familyObject,
		relationshipId = relationObject,
		patientId = pvUser
			)
		return redirect('/coversheet/')
	else:

		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def coversheeet_update(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)

	if request.method == 'POST':

		form = request.POST

		started_on = form['started']
		current_status = form['current']
		resolved_on = form['resolved']

		info_coversheet = PvMedicalHistory.objects.get(id = form['myId'])
		info_coversheet.started_on = started_on
		info_coversheet.current_status = current_status
		info_coversheet.resolved_on =resolved_on
		info_coversheet.save()
		return redirect('/coversheet/')
	else:
		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def coversheet_update1(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)

	if request.method == 'POST':

		form = request.POST
		
		surgery = form['surgery']
		surgery_date = form['surgery_dat']

		info_coversheet1 = PvSurgicalHistory.objects.get(id = form['myid'])
		info_coversheet1.surgicalhistoryId = surgery
		info_coversheet1.surgery_date = surgery_date
		info_coversheet1.save()
		return redirect('/coversheet/')

	else:
		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def coversheet_update2(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)

	if request.method == 'POST':

		form = request.POST

		familyOjbect = FamilyhistoryMaster.objects.get(name = form['problems'])
		relationObjects = RelationshipMaster.objects.get(name = form['Relationship'])

		info_coversheet2 = PvFamilyHistory.objects.get(id = form['my_ids'])
		info_coversheet2.familyhistoryId = familyOjbect
		info_coversheet2.relationship = relationObjects
		info_coversheet2.save()
		return redirect('/coversheet/')
	else:

		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def coversheeet_delete(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)

	if request.method == 'POST':

		form = request.POST

		

		info_coversheet = PvMedicalHistory.objects.get(id = form['myId1'])
		
		info_coversheet.delete()
		return redirect('/coversheet/')
	else:
		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def coversheeet_delete1(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)

	if request.method == 'POST':

		form = request.POST
		
		
		info_coversheet1 = PvSurgicalHistory.objects.get(id = form['myId2'])
	
		info_coversheet1.delete()
		return redirect('/coversheet/')
	else:
		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def coversheet_delete2(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)

	if request.method == 'POST':

		form = request.POST

		
		info_coversheet2 = PvFamilyHistory.objects.get(id = form['myId3'])
		
		info_coversheet2.delete()
		return redirect('/coversheet/')
	else:

		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def coversheet_update3(request):
	pvUser = request.user.pvuser
	medicals = PvMedicalHistory.objects.filter(patientId=pvUser)
	surgeries = PvSurgicalHistory.objects.filter(patientId=pvUser)
	families = PvFamilyHistory.objects.filter(patientId=pvUser)
	socials = PvSocialHistory.objects.filter(patientId=pvUser)

	if request.method == 'POST':

		form = request.POST
		alcohoUsage = form['alcohol_usage']
		drinksPerWeek = form['drinks']
		tobacoUsage = form['tobaco_usage']
		tobacoQuitDate = form['tobaco_quit_date']
		drugUsage = form['drug_usage']
		drugDetails = form['drug_details']

		info_updatesheet3 = PvSocialHistory.objects.get(id = form['mysocial'])
		
		info_updatesheet3.alcoholUsage = alcohoUsage
		info_updatesheet3.drinksPerWeek = drinksPerWeek
		info_updatesheet3.tobacoUsage = tobacoUsage
		info_updatesheet3.tobacoQuitDate = tobacoQuitDate
		info_updatesheet3.drugUsage = drugUsage
		info_updatesheet3.drugDetails = drugDetails

		info_updatesheet3.save()
		return redirect('/coversheet/')
	else:

		return HttpResponse('403 bad request')

@csrf_exempt
@login_required(login_url='/login')
def coversheet_personal(request):
	response = {}
	details = request.user.pvuser
	profiles = PvProfile.objects.filter(patientId=pvUser)

	if request.method =='POST':

		form = request.POST
		countryObjects = CountryMaster.objects.get(name = form['country'])
		stateObjects = StateMaster.objects.get(name = form['state'])
		cityObjects = CityMaster.objects.get(name = form['city'])
		address = form['address']
		genderObjects = GenderMaster.objects.get(name = form['genders'])

		personal1 = PvProfile.objects.get(id = form['mysocial'])

		personal1.gender = genderObjects
		personal1.countryId = countryObjects
		personal1.stateId = stateObjects
		personal1.cityId = cityObjects
		personal1.address = address
		personal1.save()
		return redirect('/coversheet/')
	else:

		return HttpResponse('403 bad request')

@login_required(login_url = "/login/")
def show_dashboard(request):
	pvUser = request.user.pvuser
	first_name = pvUser.user.first_name
	print(pvUser.email)
	return render(request,'dashboard1.html',{'first_name':first_name,'url':get_gravatar_url(pvUser.email, size=150)})