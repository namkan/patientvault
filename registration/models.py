from __future__ import unicode_literals
import datetime 
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import utc

# Create your models here.
class GenderMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

class RelationshipMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

class CountryMaster(models.Model):
	name = models.CharField(max_length=50)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

class StateMaster(models.Model):
	name = models.CharField(max_length=30)
	country = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

class CityMaster(models.Model):
	name = models.CharField(max_length=30)
	state = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

class MedicalhistoryMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

class SurgicalhistoryMaster(models.Model):
	name = models.CharField(max_length=100)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=100)
	def __str__(self):
		return '%s' % (self.name)

class FamilyhistoryMaster(models.Model):	
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

#Model to save user's account details	
class PvUser(models.Model):
	userId = models.AutoField(primary_key=True)
	user = models.OneToOneField(User,null = True, blank = True)
	#first_name = models.CharField(max_length=50)
	#last_name = models.CharField(max_length=50,default = '')
	mobile_number = models.BigIntegerField(unique = True)
	email = models.CharField(max_length=50)
	activationToken = models.CharField(max_length = 20,null=True,blank=True)
	activationAttempts = models.IntegerField(default=0,null=True,blank=True)
	isProfileComplete = models.BooleanField(default = False)
	activeYesNo = models.BooleanField(default = False)
	#otpTime = models.DateTimeField(null = True,blank = True)
	lastModifiedDateTime = models.DateTimeField(auto_now_add = True)
	pTime = models.DateTimeField(null = True,blank = True)
	# otpTime = models.DateTimeField(null = True, blank = True)
	class meta:
		db_table='PvUser'
	def otpValidTime(self,minutes):
		now = datetime.datetime.utcnow().replace(tzinfo = utc)
		timediff = now - self.pTime
		print(timediff.total_seconds())
		if timediff.total_seconds() > minutes*60:
			return False
		else:
			return True	
	def __str__(self):
		return '%s %s %s' % (self.user.username,self.user.first_name,self.email)	

#Patient's Profile
class PvProfile(models.Model):
	userId = models.OneToOneField(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	dob	= models.DateField(null = True, blank = True)
	profilePhoto = models.TextField(null = True, blank = True)	
	gender = models.ForeignKey(GenderMaster,on_delete=models.CASCADE, null = True, blank = True)
	countryId = models.ForeignKey(CountryMaster,on_delete=models.CASCADE, null = True, blank = True)
	stateId = models.ForeignKey(StateMaster,on_delete=models.CASCADE, null = True, blank = True)
	cityId = models.ForeignKey(CityMaster,on_delete=models.CASCADE, null = True, blank = True)
	address = models.CharField(max_length=100, null = True, blank = True)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField(null = True, blank = True)
	class meta:
		db_table='PvProfile'
	# def __str__(self):
	# 	return '%s %s %s' % (self.userId.user.username,self.userId.user.first_name,self.userId.email)

class PvFamilyRelationship(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	relativeName = models.CharField(max_length = 30, null = True, blank = True)
	relationshipId = models.ForeignKey(RelationshipMaster,on_delete=models.CASCADE, null = True, blank = True)
	relative = models.ForeignKey(PvUser, related_name = "relative", blank = True, null = True)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField(blank = True, null = True)
	
class PvSocialHistory(models.Model):
	patientId = models.OneToOneField(PvUser,on_delete=models.CASCADE)
	alcoholUsage = models.IntegerField(null = True,blank = True)
	drinksPerWeek = models.IntegerField(null = True, blank = True)
	tobacoUsage = models.IntegerField(null = True, blank = True)
	tobacoQuitDate = models.DateField(blank = True, null = True)
	drugUsage = models.IntegerField(null = True, blank = True)
	#drugQuitDate = models.DateField(blank = True, null = True)
	drugDetails = models.CharField(max_length = 250)
	shareYesNo = models.BooleanField(default = False)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField()

class PvMedicalHistory(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	mediacalHistoryId = models.ForeignKey(MedicalhistoryMaster,on_delete=models.CASCADE, null = True, blank = True)
	sharedYesNo = models.BooleanField(default=False)
	activeYesNo = models.BooleanField(default=True)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField()

class PvSurgicalHistory(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	surgicalhistoryId = models.ForeignKey(SurgicalhistoryMaster,on_delete=models.CASCADE, null = True, blank = True)	
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField(default=False)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField()

class PvFamilyHisotry(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE)	
	familyhistoryId = models.ForeignKey(FamilyhistoryMaster,on_delete=models.CASCADE)
	relationshipId = models.ForeignKey(RelationshipMaster,on_delete=models.CASCADE)
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField()
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField()
