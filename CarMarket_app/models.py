from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Car(models.Model):
    description = models.CharField(max_length=75)
    mileage = models.CharField(max_length=10)
    publish_on = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='car_pics')
    about = models.TextField()
    car_model= models.CharField(max_length=4)
    car_gear = (
        ('Auto', 'Auto'),
        ('Manual', 'Manual')
    )
    car_gear=models.CharField(max_length=6, choices=car_gear, default='Auto' )
    car_price = models.CharField(max_length=10)
    def get_absolute_url(self):
        return reverse('detailes', args=[str(self.id)])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)

    genders = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = models.CharField(max_length=1, choices=genders)

    def __str__(self):
        return self.user.username