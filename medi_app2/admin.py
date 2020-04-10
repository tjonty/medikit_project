from django.contrib import admin
from .models import PatientProfileInfo,DoctorProfileInfo,RecordInfo,LabInfo


# Register your models here.

admin.site.register(PatientProfileInfo)
admin.site.register(DoctorProfileInfo)
admin.site.register(RecordInfo)
admin.site.register(LabInfo)
