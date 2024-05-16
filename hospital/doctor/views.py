

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from users.models import Userprofile

from appointments.models import Appointment


# Create your views here.
def doctor_home(request):
    return render(request,'doctor_home.html')


@login_required
def update_doctor_profile(request):
    doctor = Userprofile.objects.get(user=request.user)
    if request.method == 'POST':
        doctor.phonenumber = request.POST.get('phonenumber')
        doctor.specialization = request.POST.get('specialization')
        doctor.save()
    return render(request,'update_doctor_profile.html', {'doctor': doctor})


@login_required
def delete_profile(request, user_id):
    if request.method == 'GET':
        user_profile = Userprofile.objects.get(user_id=user_id)
        user_profile.user.delete()
        return redirect('signout')
    return redirect('home')

def view_appointments(request):
    doctor = request.user.userprofile
    doctor_name = doctor.firstname + " " + doctor.lastname
    doctor_email = doctor.email
    doctor_phone = doctor.phonenumber

    upcoming_appointments = Appointment.objects.filter(doctor=doctor_name, status=True,
                                                       appointment_date__gte=timezone.now())

    previous_appointments = Appointment.objects.filter(doctor=doctor_name, status=False).order_by('-appointment_date')

    v_appointments = Appointment.objects.filter(doctor=doctor_name)
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        prescription = request.POST.get('prescription')
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.prescription = prescription
        appointment.doctor_email = doctor_email
        appointment.doctor_phonenumber = doctor_phone
        appointment.status = False
        appointment.save()

    return render(request, 'doctor_view_appointments.html', {'upcoming_appointments': upcoming_appointments, 'previous_appointments': previous_appointments})
