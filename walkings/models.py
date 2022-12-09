from django.db import models
from django.conf import settings
from accounts.models import Dog
import datetime

# max_length 수정함
class Park(models.Model):
    manageNo = models.CharField(max_length=200)
    parkName = models.CharField(max_length=300)
    parkType = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    size = models.CharField(max_length=200)


# Create your models here.
class Dogroup(models.Model):
    dogs = models.ManyToManyField(Dog, related_name="joindogs")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField(max_length=20)
    membercnt = models.IntegerField(default=5)
    create_at = models.DateTimeField(auto_now_add=True)
    join = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="joiner")


class Mylotations(models.Model):
    location = models.CharField(max_length=50)
