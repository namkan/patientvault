from django import forms

class RegistrationForm(forms.Form):

    first_name = forms.CharField(label='',
    	widget=forms.TextInput(attrs={'name':'first_name','class': 'form-control','required':'true','placeholder':'First Name',}))

    last_name = forms.CharField(label='',
    	widget=forms.TextInput(attrs={'name':'last_name','class': 'form-control', 'required':'true', 'placeholder':'Last Name'}))

    email = forms.EmailField(label='',
    	widget=forms.TextInput(attrs={'name':'email','class': 'form-control','type':'email', 'required':'false','placeholder':"Email"}))

    mobile_number = forms.IntegerField(label='',
    	widget=forms.TextInput(attrs={'name':'phone','class': 'form-control','type':'number', 'required':'true','placeholder':"Mobile Number",'maxlength':'10'}))

    password = forms.CharField(label='',
    	widget=forms.PasswordInput(attrs={'name':'password','class': 'form-control','type':'password', 'required':'true','placeholder':"Password",'id':'password'}))
    confpassword = forms.CharField(label='',
    	widget=forms.PasswordInput(attrs={'name':'cpassword','class': 'form-control','type':'password', 'required':'true','placeholder':"Confirm Password"}))
'''
class OTPValidationForm(forms.Form):
	OTP = forms.IntegerField(label = "Enter OTP here: ",
		widget=forms.TextInput(attrs={'class': 'validation','type':'number', 'required':'true','maxlength':'8'}))   
'''		