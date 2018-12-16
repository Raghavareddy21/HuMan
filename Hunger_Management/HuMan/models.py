from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
Types=(('V', 'Vegitarian'),('N', 'NonVegitarian'))
class FoodDiscription(models.Model):
    name=models.CharField(max_length=200)
    cooking_date=models.DateTimeField(help_text="Please enter the date the food was made here")
    expiry_date=models.DateTimeField(help_text="Please enter the date the food is expected to expire")
    lat=models.FloatField()
    lon=models.FloatField()
    quantity=models.IntegerField(help_text="please enter how many number of people it can feed")
    type=models.CharField(max_length=7,choices=Types)
    def __str__(self):
        return self.name
class Otherdetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
