from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from django.http import JsonResponse
from django.shortcuts import render, redirect
from management.models import Department
from users.models import Userprofile

from .models import Appointment

@login_required
def appointment(request):
    departments = Department.objects.all().values('id', 'department')
    patient = Userprofile.objects.get(user=request.user)

    if request.method == 'POST':
        department_id = request.POST.get('department')
        department = Department.objects.get(id=department_id)
        doctor = request.POST.get('doctor')
        print(doctor)

        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        symptoms = request.POST.get('symptoms')

        username = patient.username

        appointment = Appointment.objects.create(
            patient_name=f"{patient.firstname} {patient.lastname}",
            patient_username=username,
            department=department,
            doctor=doctor,
            patient_phonenumber=patient.phonenumber,
            patient_email=patient.email,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            symptoms=symptoms,
            status=True
        )
        return redirect('patient_view_appointments')

    return render(request, 'appointment.html', {'departments': departments, 'patient': patient})


def get_doctors(request):
    department_id = request.GET.get('department_id')
    doctors = Userprofile.objects.filter(department_id=department_id, user_type='Doctor')
    doctor_list = [{'id': doctor.id, 'name': f'{doctor.firstname} {doctor.lastname}'} for doctor in doctors]
    return JsonResponse({'doctors': doctor_list})



