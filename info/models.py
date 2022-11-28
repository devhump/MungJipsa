from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)


class Deserted(models.Model):
    kindCd = models.CharField(max_length=100)
    colorCd = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    weight = models.CharField(max_length=30)
    happenDt = models.DateField()
    happenPlace = models.CharField(max_length=100)
    noticeSdt = models.DateField()
    noticeEdt = models.DateField()
    processState = models.CharField(max_length=50)
    sexCd = models.CharField(max_length=20)
    neuterYn = models.CharField(max_length=20)
    specialMark = models.CharField(max_length=200)
    careNm = models.CharField(max_length=100)
    careTel = models.CharField(max_length=100)
    careAddr = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=255)
