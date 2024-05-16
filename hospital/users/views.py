from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from management.models import Department
from .models import Userprofile
from django.shortcuts import render, redirect


def signup(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phone')
        cpassword = request.POST.get('cpassword')
        usertype = request.POST.get('select')
        gender = request.POST.get('gender')

        if password != cpassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            userprofile = Userprofile.objects.create(user_type=usertype, firstname=firstname, lastname=lastname, username=username, email=email, phonenumber=phonenumber, gender=gender, user=user, status=False)
            userprofile.save()
            print(request.POST)
            return redirect('signin')

        except Exception as e:
            return render(request, 'signup.html')
    return render(request, 'signup.html', {'departments': departments})


def signin(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user_profile = Userprofile.objects.get(user=user)


            if user_profile.status:
                if user_profile.user_type == 'Patient':
                    return render(request, 'patient_home.html', {'departments': departments})

                elif user_profile.user_type == 'Doctor':
                    return render(request, 'doctor_home.html', {'departments': departments})

            else:
                return render(request, 'user_wait_approval.html', {'departments': departments})
        else:
            messages.error(request, 'Invalid password or username')
            return redirect('signin')

    return render(request, 'signin.html', {'departments': departments})


def user_wait_approval(request):
    departments = Department.objects.all()
    return render(request, 'user_wait_approval.html', {'departments': departments})


def signout(request):
    logout(request)
    return redirect('home')