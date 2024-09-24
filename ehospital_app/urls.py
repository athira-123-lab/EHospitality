
from django.urls import path
from . import views

from .views import *


urlpatterns = [

    path('',views.Register,name='about'),
    path('home/',views.Home,name='home'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout_admin,name='logout'),
    path('patient_details/',views.Patient_details,name='patient_details'),
    path('add_patient/',views.Add_patient,name='add_patient'),
    path('delete_patient(<int:pid>)/',views.Delete_patient,name='delete_patient'),
    path('schedule/',views.Schedule,name='schedule'),
    path('booking/',views.Booking,name='booking'),
    path('delete_appointment(<int:pid>)/',views.Delete_appointment,name='delete_appointment'),
    path('view_prescription/',views.View_prescription,name='view_prescription'),
    path('add_prescription/',views. Add_prescription, name='add_prescription'),
    path('delete_prescription(<int:pid>)/',views.Delete_appointment, name='delete_prescription'),
]