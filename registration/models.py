from __future__ import unicode_literals
import datetime 
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import utc

# Create your models here.
class haha(models.Model):
	name = models.CharField(max_length=30)
	# tis = models.CharField(max_length=30,null = True)

class GenderMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class RelationshipMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class CountryMaster(models.Model):
	name = models.CharField(max_length=50)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class StateMaster(models.Model):
	name = models.CharField(max_length=30)
	country = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class CityMaster(models.Model):
	name = models.CharField(max_length=30)
	state = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class MedicalhistoryMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class SurgicalhistoryMaster(models.Model):
	name = models.CharField(max_length=100, null = True, blank  = True)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=100,null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class FamilyhistoryMaster(models.Model):	
	name = models.CharField(max_length=100)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=100,null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

#Model to save user's account details	
class PvUser(models.Model):
	user = models.OneToOneField(User,null = True, blank = True)
	mobile_number = models.BigIntegerField(unique = True)
	email = models.CharField(max_length=50)
	aadhar_no = models.BigIntegerField(null = True, blank = True)
	activationToken = models.CharField(max_length = 20,null=True,blank=True)
	activationAttempts = models.IntegerField(default=0,null=True,blank=True)
	isProfileComplete = models.BooleanField(default = False)
	activeYesNo = models.BooleanField(default = False)
	shareSocial = models.BooleanField(default = True)
	shareMedical = models.BooleanField(default = True)
	shareSurgical = models.BooleanField(default = True)
	shareFamily = models.BooleanField(default = True)
	lastModifiedDateTime = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	pTime = models.DateTimeField(null = True,blank = True)
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
		return '%s %s' % (self.user.username,self.email)	

#Patient's Profile
class PvProfile(models.Model):
	userId = models.OneToOneField(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	dob	= models.DateField(null = True, blank = True)
	profilePhoto = models.URLField(null = True, blank = True)	
	gender = models.ForeignKey(GenderMaster,on_delete=models.CASCADE, null = True, blank = True)
	countryId = models.ForeignKey(CountryMaster,on_delete=models.CASCADE, null = True, blank = True)
	stateId = models.ForeignKey(StateMaster,on_delete=models.CASCADE, null = True, blank = True)
	cityId = models.ForeignKey(CityMaster,on_delete=models.CASCADE, null = True, blank = True)
	address = models.CharField(max_length=100, null = True, blank = True)
	# lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField(auto_now_add=True, null = True, blank = True)
	class meta:
		db_table='PvProfile'
	def __str__(self):
		return '%s %s %s' % (self.userId.user.username,self.userId.user.first_name,self.userId.email)

class PvFamilyRelationship(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	relativeName = models.CharField(max_length = 30, null = True, blank = True)
	relationshipId = models.ForeignKey(RelationshipMaster,on_delete=models.CASCADE, null=True, blank=True)
	relative = models.ForeignKey(PvUser, related_name = "relative", blank = True, null = True)
	# lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField(auto_now_add = True,blank = True, null = True)
	
class PvSocialHistory(models.Model):
	patientId = models.OneToOneField(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	alcoholUsage = models.IntegerField(null = True,blank = True)
	drinksPerWeek = models.IntegerField(null = True, blank = True)
	tobacoUsage = models.IntegerField(null = True, blank = True)
	tobacoQuitDate = models.CharField(max_length= 100,blank = True, null = True)
	drugUsage = models.IntegerField(null = True, blank = True)
	drugQuitDate = models.DateField(blank = True, null = True)
	drugDetails = models.CharField(max_length = 250,null= True, blank = True)
	sharedYesNo = models.BooleanField(default = True)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField(auto_now_add=True, null = True, blank = True)

class PvMedicalHistory(models.Model):
	mm = (('Active',1),('Resolved',2))
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	mediacalHistoryId = models.ForeignKey(MedicalhistoryMaster,on_delete=models.CASCADE, null = True, blank = True)
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField(default=True)
	current_status = models.CharField(choices=mm,max_length = 100, null = True, blank = True)
	started_on = models.DateField(null = True, blank = True)
	resolved_on = models.DateField(null = True, blank = True)
	lastModifiedDateTime = models.DateTimeField(null = True, blank = True)

class PvSurgicalHistory(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE, null = True, blank = True)
	surgicalhistoryId = models.ForeignKey(SurgicalhistoryMaster,on_delete=models.CASCADE, null = True, blank = True)	
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField(default=False)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField(auto_now_add=True, null = True, blank = True)

class PvFamilyHistory(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE, null = True, blank = True)	
	familyhistoryId = models.ForeignKey(FamilyhistoryMaster,on_delete=models.CASCADE)
	familyhistoryStatus = models.CharField(max_length = 10, null = True, blank = True)
	relationshipId = models.ForeignKey(RelationshipMaster,on_delete=models.CASCADE, null = True, blank = True)
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField(default = False)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField(auto_now_add=True, null = True, blank = True)
