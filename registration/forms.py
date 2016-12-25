from django import forms

class PvUser(forms.Form):
    name = forms.CharField(max_length=50)
	phoneNo = forms.IntegerField()
	email = forms.CharField(max_length=15)
	password = forms.CharField(max_length=128)
	activationToken = forms.CharField(max_length = 20)
	activationAttempts = forms.IntegerField()
	activeYesNo = forms.BooleanField()
	lastModifiedDateTime = forms.DateTimeField()
