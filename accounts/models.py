from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings
from django import forms

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    profile = ProcessedImageField(
        upload_to="images/profile",
        blank=True,
        processors=[Thumbnail(100, 100)],
        format="JPEG",
        options={"quality": 90},
    )
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    # like_users = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name="like_articles"
    # )
    # bookmark_users = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name="bookmark_articles"
    # )
    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"





class Profile(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="User"
    )
    images = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 50},
    )


DOGTYPE_CHOICES = (
    ("소형", "소형"),
    ("중형", "중형"),
    ("대형", "대형"),
)

GENDER_CHOICES = (
    ("수컷", "수컷"),
    ("암컷", "암컷"),
)


class Dog(models.Model):
    name = models.CharField(max_length=255)
    dogphoto = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 50},
    )
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    neutered = models.BooleanField(default=False)
    age = models.PositiveIntegerField(default=0)

    # 체크박스로 변경 고민중
    personality = models.CharField(max_length=255)
    dogtype = models.CharField(max_length=255, choices=DOGTYPE_CHOICES)
