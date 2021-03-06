from django import forms

class RegistrationForm(forms.Form):

    first_name = forms.CharField(label='',
    	widget=forms.TextInput(attrs={'name':'first_name','id':'first_name','class': 'form-control','required':'true','placeholder':'First Name',}))

    last_name = forms.CharField(label='',
    	widget=forms.TextInput(attrs={'name':'last_name','id':'last_name','class': 'form-control', 'required':'true', 'placeholder':'Last Name'}))

    email = forms.EmailField(label='',
    	widget=forms.TextInput(attrs={'name':'email','id':'email','class': 'form-control','type':'email', 'required':'false','placeholder':"Email"}))

    mobile_number = forms.IntegerField(label='',
    	widget=forms.TextInput(attrs={'name':'mobile_number','id':'phone','class': 'form-control', 'required':'true','placeholder':"Mobile Number",'maxlength':10}))

    password = forms.CharField(label='',
    	widget=forms.PasswordInput(attrs={'name':'password','class': 'form-control','type':'password', 'required':'true','placeholder':"Password",'id':'password'}))
    cpassword = forms.CharField(label='',
    	widget=forms.PasswordInput(attrs={'name':'cpassword','id':'cpassword','class': 'form-control','type':'password', 'required':'true','placeholder':"Confirm Password"}))


    