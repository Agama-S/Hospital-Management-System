from django.db import models

# Create your models here.
class Appointment(models.Model):
    patient_name = models.CharField(max_length=60)
    patient_username = models.CharField(max_length=40,null=True,blank=True)

    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    patient_phonenumber = models.IntegerField()
    patient_email = models.EmailField()
    doctor_phonenumber = models.IntegerField(null=True, blank=True)
    doctor_email = models.EmailField(null=True, blank=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    symptoms = models.TextField()
    prescription = models.TextField()
    status = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Appointment on "+str(self.appointment_date)




class Bill(models.Model):

    patient_name=models.CharField(max_length=40)
    Doctor_name=models.CharField(max_length=40)

    phonenumber = models.CharField(max_length=20,null=True, blank=True)
    symptoms = models.CharField(max_length=100,null=True, blank=True)

    admit_date=models.DateField(null=True, blank=True)
    discharge_date=models.DateField(null=True, blank=True)
    day_spent=models.PositiveIntegerField(null=True, blank=True)

    room_charge=models.PositiveIntegerField(null=True, blank=True)
    medicine_cost=models.PositiveIntegerField(null=True, blank=True)
    doctor_fee=models.PositiveIntegerField(null=True, blank=True)
    other_charge=models.PositiveIntegerField(null=True, blank=True)
    total=models.PositiveIntegerField(null=False, blank=True)


