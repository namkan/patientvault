from django.contrib import admin
from .models import *

admin.site.register(PvUser)
# Register your models here.
admin.site.register(PvProfile)
admin.site.register(PvFamilyRelationship)
admin.site.register(PvSocialHistory)
admin.site.register(PvMedicalHistory)
admin.site.register(PvSurgicalHistory)
admin.site.register(PvFamilyHisotry)
admin.site.register(GenderMaster)
admin.site.register(RelationshipMaster)
admin.site.register(CountryMaster)
admin.site.register(StateMaster)
admin.site.register(CityMaster)
admin.site.register(MedicalhistoryMaster)
admin.site.register(SurgicalhistoryMaster)
admin.site.register(FamilyhistoryMaster)