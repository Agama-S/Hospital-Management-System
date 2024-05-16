from django.urls import path
from .import views

urlpatterns = [
    path('appointments/', views.appointment, name='appointment'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),

]