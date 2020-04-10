from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import PatientProfileInfoForm,DoctorProfileInfoForm,RecordInfoForm,UserInfoForm,LabInfoForm,ArticleForm,CategoryForm

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
# Create your views here.

def doctor(request):
    return render(request,'medi_app2/doctor.html')

def drug_approvals(request):
    return render(request,'medi_app2/drug_approvals.html')

def MediKit(request):
    return render(request,'medi_app2/MediKit.html')

def specialist(request):
    return render(request,'medi_app2/specialist.html')

def lab(request):
    return render(request,'medi_app2/lab.html')

class recordCreateView(CreateView):
    fields = ('Patient_Personal_name','Doctor_Personal_name','Appointment_Date','Disease','Medicine_Prescription','Report_Name','Report_Document')
    model = models.RecordInfo

class patientListView(ListView):
    context_object_name = 'record_list'
    model = models.RecordInfo

class patientDetailView(DetailView):
    context_object_name = 'record_detail'
    model = models.RecordInfo
    template_name = 'medi_app2/recordinfo_detail.html'

class DoctorListView(ListView):
    context_object_name = 'doctor_list'
    models = models.DoctorProfileInfo

    def get_queryset(self):
        return models.DoctorProfileInfo.objects.all()

class articleListView(ListView):
    template_name = 'medi_app2/articlelist.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return models.Article.objects.all().order_by('-id')


class articleDetailView(DetailView):
    template_name = 'medi_app2/articledetail.html'
    models = models.Article
    context_object_name = 'article_detail'

    def get_queryset(self):
        return models.Article.objects.all().order_by('-id')


class articleCreateView(CreateView):
    template_name = 'medi_app2/articlecreate.html'
    form_class = ArticleForm
    success_url = "/articlelist/"

class catedoryCreateView(CreateView):
    template_name = 'medi_app2/categorycreate.html'
    form_class = CategoryForm
    success_url = "/articlelist/"

class articleUpdateView(UpdateView):
    template_name = 'medi_app2/articlecreate.html'
    form_class = ArticleForm
    models = models.Article
    success_url = "/articlelist/"

    def get_queryset(self):
        return models.Article.objects.all().order_by('-id')


class articleDeleteView(DeleteView):
    template_name = 'medi_app2/articledelete.html'
    models = models.Article
    success_url = "/articlelist/"

    def get_queryset(self):
        return models.Article.objects.all().order_by('-id')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('medi_app2:MediKit'))
            else:
                return HttpResponse("Account not active")
        else:
            return HttpResponseRedirect(reverse('medi_app2:login'))

    else:
        return render(request, 'medi_app2/login.html')

@login_required
def special(request):
    return HttpResponse("<h1> You are logged in</h1>")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('medi_app2:MediKit'))

def signup(request):
    return render(request,'medi_app2/signup.html')

def doctor_signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserInfoForm(data=request.POST)
        doctor_form = DoctorProfileInfoForm(request.POST,request.FILES)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.user = user

            if 'Doctor_Certificate' in request.FILES:
                doctor.Doctor_Certificate = request.FILES['Doctor_Certificate'***REMOVED***

            if 'Doctor_Photo' in request.FILES:
                doctor.Doctor_Photo = request.FILES['Doctor_Photo'***REMOVED***

            doctor.save()
            registered = True
        else:
            print(user_form.errors,doctor_form.errors)
    else:
        user_form = UserInfoForm()
        doctor_form = DoctorProfileInfoForm()

    return render(request,'medi_app2/doctor_signup.html',{
        'user_form':user_form,'doctor_form':doctor_form,'registered':registered
***REMOVED***)

def patient_signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserInfoForm(data=request.POST)
        patient_form = PatientProfileInfoForm(data=request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            registered = True
        else:
            print(user_form.errors, patient_form.errors)
    else:
        user_form = UserInfoForm()
        patient_form = PatientProfileInfoForm()

    return render(request, 'medi_app2/patient_signup.html', {
        'user_form': user_form, 'patient_form': patient_form, 'registered': registered
***REMOVED***)

def lab_signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserInfoForm(data=request.POST)
        lab_form = LabInfoForm(request.POST,request.FILES)
        if user_form.is_valid() and lab_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            lab = lab_form.save(commit=False)
            lab.user = user

            if 'Lab_Certificate' in request.FILES:
                lab.Lab_Certificate = request.FILES['Lab_Certificate'***REMOVED***

            lab.save()
            registered = True
        else:
            print(user_form.errors,lab_form.errors)
    else:
        user_form = UserInfoForm()
        lab_form = LabInfoForm()

    return render(request,'medi_app2/lab_signup.html',{
        'user_form':user_form,'lab_form':lab_form,'registered':registered
***REMOVED***)

def email_to(request):
    registered = False
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = request.POST.get('from_email')
        from_def_email = settings.DEFAULT_FROM_EMAIL
        to_email = [request.POST.get('to_email')***REMOVED***
        contact_message_1 = message + " \n from:\n name: "+name+"\n Email: "+from_email + "\n"
        contact_message_2 = settings.ACCOUNT_EMAIL_SUBJECT_POSTFIX_1 + "\n" + settings.ACCOUNT_EMAIL_SUBJECT_POSTFIX_2
        contact_message = contact_message_1 + contact_message_2
        send_mail(subject,contact_message,from_def_email,to_email,fail_silently=True)
        registered = True
        return render(request,"medi_app2/email.html",{
            'registered' : registered
    ***REMOVED***)

    return render(request,'medi_app2/email.html',{
        'registered': registered
***REMOVED***)