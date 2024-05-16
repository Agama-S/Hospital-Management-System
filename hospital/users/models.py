from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from management.models import Department


class Userprofile(models.Model):
    SELECT_CHOICES = (
        ("Doctor", "Doctor"),
        ("Patient", "Patient")
    )

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Prefer not to say", "Prefer not to say")
    )


    user_type = models.CharField(max_length=10, choices=SELECT_CHOICES)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='static/prof_pic', blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    attendance = models.IntegerField(null=True, blank=True)
    specialization = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

@receiver(pre_delete, sender=Userprofile)
def delete_user_on_h_user_delete(sender, instance, **kwargs):

    user = instance.user
    pre_delete.disconnect(delete_user_on_h_user_delete, sender=Userprofile)
    user.delete()
    pre_delete.connect(delete_user_on_h_user_delete, sender=Userprofile)


