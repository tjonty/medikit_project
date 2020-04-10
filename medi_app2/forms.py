from django import forms
from .models import User,PatientProfileInfo,DoctorProfileInfo,RecordInfo,LabInfo,Article,Category
from django.contrib.auth.models import Group

class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class PatientProfileInfoForm(forms.ModelForm):
    class Meta():
        model = PatientProfileInfo
        fields = ('Patient_Personal_name','Patient_Age','Patient_Address','Patient_Pin','Patient_State')

class DoctorProfileInfoForm(forms.ModelForm):
    class Meta():
        model = DoctorProfileInfo
        fields = ('Doctor_Personal_name', 'Doctor_experience', 'Doctor_Education', 'Doctor_Speciality', 'Hospital_Address', 'Hospital_Pin', 'Hospital_State', 'Doctor_Certificate', 'Doctor_Photo')

class LabInfoForm(forms.ModelForm):
    class Meta():
        model = LabInfo
        fields = ('Person_name','Address','Pincode','Lab_Certificate')

class RecordInfoForm(forms.ModelForm):
    Medicine_Prescription = forms.CharField(widget=forms.Textarea)
    class Meta():
        model = RecordInfo
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = ('Title', 'Category', 'Image', 'Content', 'Author')

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = ('Title',)

