from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager



class User(AbstractUser):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254,unique=True)
    password = models.CharField( max_length=500)
    username = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()