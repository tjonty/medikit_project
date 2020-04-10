from django.urls import path,include
from . import views

from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'medi_app2'

urlpatterns = [
    path('',views.MediKit,name='MediKit'),
    path('recordinfo_form/',views.recordCreateView.as_view(),name="recordinfo_form"),
    path('doctorprofileinfo_list/',views.DoctorListView.as_view(),name="doctorprofileinfo_list"),
    path('email',views.email_to,name="email"),
    path('recordinfo_list/',views.patientListView.as_view(),name="recordinfo_list"),
    path('recordinfo_list/<int:pk>/detail/',views.patientDetailView.as_view(),name='resouceinfo_detail'),

    path('articlelist/',views.articleListView.as_view(),name='articlelist'),
    path('articlelist/<int:pk>/detail/',views.articleDetailView.as_view(),name="articledetail"),
    path('articlelist/articlecreate/',views.articleCreateView.as_view(),name="articlecreate"),
    path('articlelist/categorycreate/',views.catedoryCreateView.as_view(),name="categorycreate"),
    path('articlelist/<int:pk>/update/',views.articleUpdateView.as_view(),name="articleupdate"),
    path('articlelist/<int:pk>/delete/',views.articleDeleteView.as_view(),name="articledelete"),

    path('drug_approvals/',views.drug_approvals,name="drug_approvals"),
    path('specialist/', views.specialist, name="specialist"),
    path('lab/',views.lab,name="lab"),
    path('signup/', include([
        path('', views.signup,name="signup"),
        path('patient_signup/',views.patient_signup,name="patient_signup"),
        path('doctor_signup/',views.doctor_signup,name="doctor_signup"),
        path('lab_signup/',views.lab_signup,name="lab_signup"),
    ***REMOVED***)),
    path('login/',views.user_login,name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('special/',views.special,name='special'),
***REMOVED***
