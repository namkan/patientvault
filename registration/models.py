from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class GenderMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

class RelationshipMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

class CountryMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

class StateMaster(models.Model):
	name = models.CharField(max_length=30)
	country = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

class CityMaster(models.Model):
	name = models.CharField(max_length=30)
	state = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

class MedicalhistoryMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

class SurgicalhistoryMaster(models.Model):
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

class FamilyhistoryMaster(models.Model):	
	name = models.CharField(max_length=30)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

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
	activeYesNo = models.BooleanField(default = False)
	lastModifiedDateTime = models.DateTimeField(auto_now_add = True)
	class meta:
		db_table='PvUser'
	def __str__(self):
		return '%s %s %s' % (self.user.username,self.user.first_name,self.email)	

class PvProfile(models.Model):
	userId = models.ForeignKey(PvUser,on_delete=models.CASCADE)
	age	= models.IntegerField()	
	gender = models.ForeignKey(GenderMaster,on_delete=models.CASCADE)
	countrtyId = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
	stateId = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
	cityId = models.ForeignKey(CityMaster,on_delete=models.CASCADE)
	address = models.CharField(max_length=100)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField()

class PvFamilyRelationship(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE)
	relativeName = models.CharField(max_length = 30)
	relationshipId = models.ForeignKey(RelationshipMaster,on_delete=models.CASCADE)
	relativeVhNo = models.CharField(max_length=10)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField()

class PvSocialHistory(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE)
	alcoholUsage = models.BooleanField()
	drinksPerWeek = models.IntegerField()
	tobacoUsage = models.BooleanField()
	tobacoQuitDate = models.DateField()
	drugUsage = models.BooleanField()
	drugQuitDate = models.BooleanField()
	drugDetails = models.CharField(max_length = 250)
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField()

class PvMedicalHistory(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE)
	mediacalHistoryId = models.ForeignKey(MedicalhistoryMaster,on_delete=models.CASCADE)
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField()
	#lastModifiedBy = models.ForeignKey(PvUser)
	lastModifiedDateTime = models.DateTimeField()

class SurgicalHistory(models.Model):
	patientId = models.ForeignKey(PvUser,on_delete=models.CASCADE)
	surgicalhistoryId = models.ForeignKey(SurgicalhistoryMaster,on_delete=models.CASCADE)	
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField()
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
