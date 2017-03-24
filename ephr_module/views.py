from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
import cloudinary,cloudinary.uploader,cloudinary.api
from .models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def uploadDocuments(request):
	if request.method == "POST":
		info_dic = None
		data = request.POST
		print(request.FILES)
		info_dic = cloudinary.uploader.upload(request.FILES['report'])
		reports = PvUploadedFiles.objects.get_or_create(
			file_name = data['Report Name'],
			file_type = data['Report Type'],
			file_url = info_dic['secure_url'],
			added_on = datetime.now().date())
		return HttpResponse('haha')
	else:
		reports = PvUploadedFiles.objects.all()
		return render(request,'upload_reports.html',{'reports':reports})

@csrf_exempt
def changeDocumentShareStatus(request):
	response = {}
	if request.method == 'POST':
		data = request.POST
		desired_model = PvUploadedFiles.objects.get(file_name = data['id'])
		desired_model.is_sharable = bool(int(data['shareStatus']))
		desired_model.save()
		response['status'] = 1
		return JsonResponse(response)
	else:
		return HttpResponse('403 bad request')
			
def labview(request):
	orders = PvLaborders.objects.all()
	results = PvLabresults.objects.all()
	return render(request,'lab_reports.html',{'info': zip(orders, results)})

def radioview(request):
	orders = PvRadorders.objects.all()
	results = PvRadresults.objects.all()
	return render(request,'lab_reports.html',{'info': zip(orders, results)})

def allergies(request):
	response = {}
	categories = AllergyCategoryMaster.objects.all()
	effects = AllergyServerityMaster.objects.all()
	if request.method == 'POST':
		form = request.POST
		substance = form["substance"]
		reaction_details = form["reaction_details"]
		categoryOjbect = AllergyCategoryMaster.objects.get(name = form['category'])
		serverityObjects = AllergyServerityMaster.objects.get(name = form['effect'])
		pv_allergy = PvAllergy.objects.create(
		Substance = substance,
		category_id = categoryOjbect,
		serverity_id = serverityObjects,
		reactions = reaction_details,
			)

		return HttpResponse('fine')

	else:
		
		return render(request,'allergies.html',{'categories':categories,'effects':effects})


def medication(request):
	response = {}
	doctors = DpUser.objects.all()
	dosages = PvPrescriptionDetails.objects.all()
	nums = PvPrescription.objects.all()
	drugs = DrugMaster.objects.all()
	names = PhUser.objects.all()


	return render(request,'medication.html',{'info' : zip(drugs,dosages,nums),'info1' : zip(nums,doctors,names)})
