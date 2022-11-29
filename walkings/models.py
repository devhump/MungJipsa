from django.db import models
from django.conf import settings
from accounts.models import Dog


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
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    datatime = models.DateTimeField()
    title = models.CharField(max_length=20)
    membercnt = models.IntegerField(default=5)


class Mylotations(models.Model):
    location = models.CharField(max_length=50)
