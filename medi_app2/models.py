from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
# Create your models here.
class PatientProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    Patient_Personal_name = models.CharField(max_length=264)
    Patient_Age = models.PositiveSmallIntegerField()
    Patient_Address = models.CharField(max_length=300)
    Patient_Pin = models.PositiveIntegerField()
    Patient_State = models.CharField(max_length=100)

    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class DoctorProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    Doctor_Personal_name = models.CharField(max_length=264)
    Doctor_experience = models.PositiveSmallIntegerField()
    Doctor_Education = models.CharField(max_length=264)
    Doctor_Speciality = models.CharField(max_length=264)
    Hospital_Address = models.CharField(max_length=300)
    Hospital_Pin = models.PositiveIntegerField()
    Hospital_State = models.CharField(max_length=100)
    Doctor_Certificate = models.FileField(upload_to='Certificate',blank=False)
    Doctor_Photo = models.ImageField(upload_to='Doctor_Pic',blank=False)

    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class LabInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    Person_name = models.CharField(max_length=264)
    Address = models.CharField(max_length=264)
    Pincode = models.PositiveIntegerField()
    Lab_Certificate = models.FileField(upload_to='media/lab_Certificate',blank = False)

    def __str__(self):
        return self.user.username


class RecordInfo(models.Model):
    Patient_Personal_name = models.CharField(max_length=264)

    Doctor_Personal_name = models.ForeignKey(DoctorProfileInfo,on_delete=models.PROTECT)
    Appointment_Date = models.DateField("Apointment_Date", default=datetime.date.today)
    Disease = models.CharField(max_length=264)
    Medicine_Prescription = models.CharField(max_length=400)
    Report_Name = models.CharField(max_length=264)
    Report_Document = models.FileField(upload_to='media/Patient_Report',blank=True)

    def __str__(self):
        return self.Patient_Personal_name

    def get_absolute_url(self):
        return reverse("medi_app2:recordinfo_form")
    
class Category(models.Model):
    Title = models.CharField(max_length=264)

    def __str__(self):
        return self.Title

class Article(models.Model):
    Title = models.CharField(max_length=264)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='blog',blank=True)
    Content = models.TextField()
    Published_Date = models.DateTimeField(auto_now=True)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    View_Count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.Title
