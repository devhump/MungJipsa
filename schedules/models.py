from django.db import models
from django.conf import settings

# Create your models here.

class Schedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    schedule = (
        ('산책', '산책'),
        ('병원', '병원'),
        ('모임', '모임'),
        ('기타', '기타'),
    )
    schedule_type = models.CharField(max_length=100, choices=schedule, null=True)
    prior = (
        ('1', "1"),
        ('2', "2"),
        ('3', "3"),
        ('4', "4"),
        ('5', "5"),
    )
    priority = models.CharField(max_length=100, choices=prior, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)