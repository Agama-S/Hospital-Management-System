from django.contrib import admin
from .models import Appointment, Bill
# Register your models here.
admin.site.register(Appointment)
admin.site.register(Bill)