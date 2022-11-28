from django.db import models

# Create your models here.
# class Dogroup(models.Model):
#     # dog = models.ForeignKey
#     # user = models.ForeignKey
#     # park = models.ForeignKey
#     datatime = models.DateTimeField()
#     title = models.CharField(max_length=20)
#     membercnt = models.IntegerField()


class Park(models.Model):
    manageNo = models.CharField(max_length=20)
    parkName = models.CharField(max_length=30)
    parkType = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
