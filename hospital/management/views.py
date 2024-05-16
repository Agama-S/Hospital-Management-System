from django.shortcuts import render
from .models import Department
from users.models import Userprofile

# Create your views here.
def home(request):
    departments = Department.objects.all()
    doctors = (Userprofile.objects.filter(user_type='Doctor').values('firstname', 'lastname', 'image', 'specialization'))
    return render(request, 'home.html', {'departments': departments, 'doctors': doctors})

