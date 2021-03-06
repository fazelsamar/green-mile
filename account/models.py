from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MyUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile-pic/')
    phone_number = models.IntegerField(null=True, blank=True)
