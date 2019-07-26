from django.db import models
from django.utils import timezone

class Car(models.Model):
    ad_description = models.CharField(max_length=75)
    mamsha = models.CharField(max_length=10)
    publish_on = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='car_pics')
    about = models.TextField()
    car_model= models.CharField(max_length=4)
    car_type = models.CharField(max_length=75)
    car_price = models.CharField(max_length=10)
