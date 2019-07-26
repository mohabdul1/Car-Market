from django.db import models
from django.utils import timezone

class Car(models.Model):
    ad_description = models.CharField(max_length=75)
    mamsha = models.IntegerField()
    publish_on = models.DateTimeField(default=timezone.now)
    added_on = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='book_pics')
    about = models.TextField()
    car_model= models.IntegerField()
    cat_type = models.IntegerField()
    car_price = models.IntegerField()
