from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=25)
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.CharField(null=True, max_length=250)
    email = models.EmailField(null=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []