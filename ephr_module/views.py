from django.shortcuts import render

# Create your views here.
def uploadDocuments(request):
	if request.method == "POST":
		pass
	else:
		return render(request,'upload_reports.html')
			