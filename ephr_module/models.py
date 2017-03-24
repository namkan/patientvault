from __future__ import unicode_literals
import datetime 
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import utc	
from registration.models import *

class PvUploadedFiles(models.Model):
	filename = models.CharField(max_length=200)
	file_type = models.CharField(max_length=100)
	file_url = models.URLField(max_length = 100,null= True,blank= True)
	added_on = models.DateField(null = True, blank = True)
	active_yesno = models.BooleanField(default = True)
	last_modified_by = models.ForeignKey(PvUser,null = True, blank = True)
	# last_modified_date_time = models.DateTimeField(null=True,blank=True)
	class meta:
		db_table='pv_uploaded_files'
	def __str__(self):
		return '%s ' % (self.filename)
 
  

		

