from __future__ import unicode_literals

from django.db import models

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
	country = models.ForiegnKey(CountryMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=True)
	lastModifiedDateTime = models.CharField(max_length=30)

class CityMaster(models.Model):
	name = models.CharField(max_length=30)
	state = models.ForiegnKey(StateMaster,on_delete=models.CASCADE)
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
	
class PvUser(models.Model):
	name = models.CharField(max_length=50)
	phoneNo = models.IntegerField()
	email = models.CharField(max_length=15)
	password = models.CharField(_('password'),max_length=128)
	activationToken = 
	activationAttempts = models.IntegerField()
	activeYesNo = models.BooleanField()
    lastModifiedDateTime = models.DateTimeField()
	class meta:
		db_table='PvUser'

class PvProfile(models.Model):
	userId = models.ForiegnKey(PvUSer,on_delete=models.CASCADE)
	age	= models.IntegerField()	
	gender = models.ForiegnKey(GenderMaster,on_delete=models.CASCADE)
	countrtyId = models.ForiegnKey(CountryMaster,on_delete=models.CASCADE)
	stateId = models.ForiegnKey(StateMaster,on_delete=models.CASCADE)
	cityId = models.ForiegnKey(CityMaster,on_delete=models.CASCADE)
	address = models.CharField(max_length=100)
	lastModifiedBy = 
	lastModifiedDateTime = models.DateTimeField()

class PvFamilyRelationship(models,Model):
	patientId = models.ForiegnKey(PvUSer,on_delete=models.CASCADE)
	relativeName = models.CharField(30)
	relationshipId = models.ForiegnKey(RelationshipMaster,on_delete=models.CASCADE)
	relativeVhNo. = models.CharField(max_length=10)
	lastModifiedBy = 
	lastModifiedDateTime = models.DateTimeField()

class PvSocialHistory(models.Model):
	patientId = models.ForiegnKey(PvUSer,on_delete=models.CASCADE)
	alcoholUsage = models.BooleanField()
	drinksPerWeek = models.IntegerField()
	tobacoUsage = models.BooleanField()
	tobacoQuitDate = models.DateField()
	drugUsage = models.BooleanField()
	drugQuitDate = models.BooleanField()
	drugDetails = models.CharField()
	lastModifiedBy = 
	lastModifiedDateTime = models.DateTimeField()

class PvMedicalHistory(models.Model):
	patientId = models.ForiegnKey(PvUSer,on_delete=models.CASCADE)
	mediacalHistoryId = models.ForiegnKey(MediclalhistoryMaster,on_delete=models.CASCADE)
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField()
	lastModifiedBy = 
	lastModifiedDateTime = models.DateTimeField()

class SurgicalHistory(models.Model):
	patientId = models.ForiegnKey(PvUSer,on_delete=models.CASCADE)
	surgicalhistoryId = models.ForiegnKey(SurgicalhistoryMaster,on_delete=models.CASCADE)	
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField()
	lastModifiedBy = 
	lastModifiedDateTime = models.DateTimeField()

class PvFamilyHisotry(models.Model):
	patientId = models.ForiegnKey(PvUSer,on_delete=models.CASCADE)	
	familyhistoryId = models.ForiegnKey(FamilyhistoryMaster,on_delete=models.CASCADE)
	relationshipId = models.ForiegnKey(RelationshipMaster,on_delete=models.CASCADE)
	sharedYesNo = models.BooleanField(default=True)
	activeYesNo = models.BooleanField()
	lastModifiedBy = 
	lastModifiedDateTime = models.DateTimeField()
