from __future__ import unicode_literals
import datetime 
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import utc	
from registration.models import *

class AllergyCategoryMaster(models.Model):
	name = models.CharField(max_length=100)
	Substance = models.CharField(max_length=200)
	active_yesNo = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s ' % (self.name)

class AllergyServerityMaster(models.Model):
	name = models.CharField(max_length=100)
	Substance = models.CharField(max_length=200)
	active_yesNo = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s ' % (self.name)

class DpUser(models.Model):
	name = models.CharField(max_length=100)
	active_yesNo = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s ' % (self.name)

class VisitStatusMaster(models.Model):
	name = models.CharField(max_length=100)
	acive_yesno = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField()
	def __str__(self):
		return '%s ' % (self.name)



class DpVisits(models.Model):
	doctor_id = models.ForeignKey(DpUser,null = True, blank = True)
	patient_id = models.ForeignKey(PvUser,null = True, blank = True)
	visit_date = models.DateTimeField()
	visit_time = models.DateTimeField()
	visit_status = models.ForeignKey(VisitStatusMaster,null = True, blank = True)
	def __str__(self):
		return 'visit with %s ' % (self.doctor_id.name)


class PvAllergy(models.Model):
	patient_id	= models.ForeignKey(PvUser,null = True, blank = True)
	substance = models.CharField(max_length=200)	
	category_id = models.ForeignKey(AllergyCategoryMaster,null = True, blank = True)
	serverity_id = models.ForeignKey(AllergyServerityMaster,null = True, blank = True)
	reactions = models.CharField(max_length=200)
	is_sharable = models.BooleanField(default=True)
	visit_id = models.ForeignKey(DpVisits,null = True, blank = True)
	active_yesno = models.BooleanField(default = False)
	created_by_doc = models.BooleanField(default = False)
	created_doc_id = models.ForeignKey(DpUser,null = True, blank = True)
	last_modified_by = models.BigIntegerField(null = True, blank = True)
	last_modified_date_time = models.DateTimeField(auto_now = True, null=True, blank=True)
	def __str__(self):
		return '%s ' % (self.id)

class Icd10(models.Model):
	code = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	active_yesNo = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s ' % (self.id)

class DiagnosisStatusMaster(models.Model):
	status = models.CharField(max_length=100)
	active_yesNo = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s ' % (self.id)



class PvProblemlist(models.Model):
	mm = (('yes',1),('no',0))
	patient_id = models.ForeignKey(PvUser,null = True, blank = True)
	freetext_yesno = models.CharField(choices = mm,null = True, blank = True,max_length=100)
	freetext_desc = models.CharField(max_length=100,null = True, blank = True)
	icd_code = models.ForeignKey(Icd10,null = True, blank = True)
	status = models.ForeignKey(DiagnosisStatusMaster,null = True, blank = True)
	shared_yesno = models.BooleanField(default = False)
	visit_id = models.ForeignKey(DpVisits,null = True, blank = True)
	created_by = models.ForeignKey(DpUser,null = True, blank = True)
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s ' % (self.id)

class PhUser(models.Model):
	name = models.CharField(max_length=100)
	acive_yesno = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField(null=True,blank=True)
	class meta:
		db_table='ph_user'
	def __str__(self):
		return '%s ' % (self.name)


class PvPrescription(models.Model):
	mm = (('open',1),('partially processed',2),('processed',3),('closed',4))
	rx_no = models.CharField(max_length=100)
	patient_id = models.ForeignKey(PvUser,null = True, blank = True)
	visit_id = models.ForeignKey(DpVisits,null = True, blank = True)
	created_by = models.ForeignKey(DpUser,null = True, blank = True)
	status = models.CharField(choices = mm,max_length = 100)
	processed_by = models.ForeignKey(PhUser,null = True, blank = True)
	is_sharable = models.BooleanField(default=True)
	created_on = models.DateTimeField(null = True,blank = True)
	def __str__(self):
		return '%s ' % (self.id)

class DrugMaster(models.Model):
	name = models.CharField(max_length=100)
	acive_yesno = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField(null = True, blank = True)
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s ' % (self.name)


class GenericMaster(models.Model):
	name = models.CharField(max_length=100)
	acive_yesno = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField()
	def __str__(self):
		return '%s ' % (self.name)

class StrengthMaster(models.Model):
	name = models.CharField(max_length=100)
	acive_yesno = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField()
	def __str__(self):
		return '%s ' % (self.name)

class DrugTypeMaster(models.Model):
	name = models.CharField(max_length=100)
	acive_yesno = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField()
	def __str__(self):
		return '%s ' % (self.name)
 

class PvPrescriptionDetails(models.Model):
	mm = (('brand based',1),('generic',2),('free text',3))
	prescription_id = models.ForeignKey(PvPrescription,null = True, blank = True)
	prescription_type = models.CharField(choices = mm,max_length = 10)
	patient_id = models.ForeignKey(PvUser,null = True, blank = True)
	drug_id = models.ForeignKey(DrugMaster,null = True, blank = True)
	generic_id = models.ForeignKey(GenericMaster,null = True, blank = True)
	free_text = models.TextField(null = True,blank = True)
	dose = models.CharField(max_length=300)
	strenght_id = models.ForeignKey(StrengthMaster,null = True, blank = True)
	drug_type = models.ForeignKey(DrugTypeMaster,null = True, blank = True)
	qnty = models.IntegerField(null = True,blank = True)
	created_on = models.DateTimeField(null = True, blank = True)	
	schedule = models.CharField(max_length=200)
	start_date = models.DateTimeField(null=True,blank=True)
	end_date = models.DateTimeField(null=True,blank=True)
	instructions = models.TextField(null = True, blank = True)
	created_by = models.ForeignKey(DpUser,null=True,blank=True)
	created_on = models.DateTimeField(null=True,blank=True)
	def __str__(self):
		return '%s ' % (self.patient_id.user.username)



class PvLaborders(models.Model):
	mm = (('ordered',1),('Inprogress',2),('processed',3))
	order_name = models.CharField(max_length = 50, null = True, blank = True)
	patient_id = models.ForeignKey(PvUser,null = True, blank = True)
	ordered_by = models.ForeignKey(DpUser,null = True, blank = True)
	ordered_to = models.ForeignKey(PhUser, related_name = 'tags', null = True, blank = True)
	order_status = models.CharField(null = True, blank = True, max_length=50, choices = mm)
	ordered_date = models.DateTimeField(null=True,blank=True)
	processed_by = models.ForeignKey(PhUser,null = True, blank = True)
	processed_on = models.DateTimeField(null=True,blank=True)
	checkbox_id = models.CharField(max_length = 50, null = True, blank = True)
	is_sharable = models.BooleanField(default = True)
	def __str__(self):
		return '%s ' % (self.id)

class PvLabresults(models.Model):
	# order_id = models.ForeignKey(PvLaborders, null = True, blank = True)
	file_path = models.CharField(max_length=100)
	def __str__(self):
		return '%s ' % (self.id)

class RdUser(models.Model):
	name = models.CharField(max_length=100)
	acive_yesno = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField()
	last_modified_date_time = models.DateTimeField(null=True,blank=True)
	
	class meta:
		db_table='rd_user'
	def __str__(self):
		return '%s ' % (self.name)

class PvRadorders(models.Model):
	mm = (('ordered',1),('Inprogress',2),('processed',3))
	order_name = models.CharField(max_length = 30, null = True, blank = True)
	patient_id = models.ForeignKey(PvUser, null = True, blank = True, max_length=100)
	ordered_by = models.ForeignKey(DpUser,null = True, blank = True)
	ordered_to = models.ForeignKey(RdUser,related_name = 'tags', null = True, blank = True)
	order_status = models.CharField(null = True, blank = True, max_length=50, choices = mm)
	ordered_date = models.DateTimeField(null=True,blank=True)
	processed_by = models.ForeignKey(RdUser,null = True, blank = True)
	processed_on = models.DateTimeField(null=True,blank=True)
	checkbox_id = models.CharField(max_length = 50, null = True, blank = True)
	is_sharable = models.BooleanField(default = True)
	def __str__(self):
		return '%s ' % (self.id)

class PvRadresults(models.Model):
	order_id = models.ForeignKey(PvRadorders,null = True, blank = True)
	file_path = models.CharField(max_length=100)
	def __str__(self):
		return '%s ' % (self.id)

class PvReminders(models.Model):
	MM = (('active',1),('closed',0))
	patient_id = models.ForeignKey(PvUser,null = True, blank = True)
	created_by = models.ForeignKey(DpUser,null = True, blank = True)
	content = models.CharField(max_length=200,null = True, blank = True)
	status = models.CharField(choices=MM, max_length=15, null = True, blank = True)
	reminder_date = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s ' % (self.id)

class PvUploadedFiles(models.Model):
	filename = models.CharField(max_length=200)
	file_type = models.CharField(max_length=100)
	file_url = models.URLField(max_length = 100,null= True,blank= True)
	added_on = models.DateField(null = True, blank = True)
	is_sharable = models.BooleanField(default = True)
	active_yesno = models.BooleanField(default = True)
	checkbox_id = models.CharField(max_length = 50, null = True, blank = True)
	last_modified_by = models.ForeignKey(PvUser,null = True, blank = True)
	last_modified_date_time = models.DateTimeField(null=True,blank=True)
	def __str__(self):
		return '%s ' % (self.filename)
 
  

		

