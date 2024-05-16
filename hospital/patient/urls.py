
from django.urls import path
from .import views

urlpatterns = [
    path('patient/', views.patient_home, name='patient_home'),
    path('update_patient_profile/', views.update_patient_profile, name='update_patient_profile'),
    path('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
    path('appointments/delete/<int:appointment_id>/', views.patient_delete_appointment, name='patient_delete_appointment'),
    path('patient_view_appointments/', views.view_appointments, name='patient_view_appointments'),
    path('patient_view_bill', views.view_bill, name='patient_view_bill')

]
