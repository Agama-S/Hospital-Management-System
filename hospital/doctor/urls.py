from django.urls import path
from .import views

urlpatterns = [
    path('doctor/', views.doctor_home, name='doctor_home'),
    path('update_doctor_profile/', views.update_doctor_profile, name='update_doctor_profile'),
    path('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
    path('doctor_view_appointments/', views.view_appointments, name='doctor_view_appointments'),

]