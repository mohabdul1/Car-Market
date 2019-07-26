from django.db import models
from django.utils import timezone

class Car(models.Model):
    #ad_description = models.CharField(max_length=75),
    mamsha = models.IntegerField()
    publish_on = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='car_pics')
    about = models.TextField()
    car_model= models.IntegerField()
    car_type = models.IntegerField()
    car_price = models.IntegerField()
