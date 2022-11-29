from django.db import models

# Create your models here.
class Dogroup(models.Model):
    dog = models.ForeignKey
    user = models.ForeignKey
    park = models.ForeignKey
    datatime = models.DateTimeField()
    title = models.CharField(max_length=20)
    membercnt = models.IntegerField(default=5)


# max_length 수정함
class Park(models.Model):
    manageNo = models.CharField(max_length=200)
    parkName = models.CharField(max_length=300)
    parkType = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    size = models.CharField(max_length=200)


class Mylotations(models.Model):
    location = models.CharField(max_length=50)
