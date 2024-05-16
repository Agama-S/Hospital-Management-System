from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from users.models import Userprofile

from appointments.models import Appointment, Bill


# Create your views here.
def patient_home(request):

    return render(request,'patient_home.html')


@login_required
def update_patient_profile(request):
    patient = Userprofile.objects.get(user=request.user)
    if request.method == 'POST':

        patient.phonenumber = request.POST.get('phonenumber')
        patient.save()

    return render(request, 'update_patient_profile.html', {'patient': patient})

@login_required
def delete_profile(request, user_id):
    if request.method == 'GET':
        user_profile = Userprofile.objects.get(user_id=user_id)
        user_profile.user.delete()
        return redirect('signout')
    return redirect('home')

def view_appointments(request):
    patient = request.user.userprofile
    print("pat", patient)
    upcoming_appointments = Appointment.objects.filter(patient_username=patient, status=True,
                                                       appointment_date__gte=timezone.now())

    previous_appointments = Appointment.objects.filter(patient_username=patient, status=False)
    v_appointments = Appointment.objects.filter(patient_username=patient)
    print(v_appointments)
    return render(request, 'patient_view_appointments.html', {'upcoming_appointments': upcoming_appointments, 'previous_appointments': previous_appointments})

def patient_delete_appointment(request, appointment_id):
    if not request.user.is_active:
        return redirect('signup')
    appointment = Appointment.objects.filter(id=appointment_id, patient_username=request.user.userprofile).first()

    if appointment:
        appointment.delete()
    return redirect('patient_view_appointments')


def view_bill(request):
    patient = Userprofile.objects.get(user=request.user)
    patient_name = patient.firstname + " " + patient.lastname
    print("p_name", patient_name)
    v_bill =Bill.objects.filter(patient_name=patient_name)
    print("v_bill", v_bill)

    return render(request, 'patient_view_bill.html', {'v_bill': v_bill})