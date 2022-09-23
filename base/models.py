from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=25, null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.CharField(null=True, max_length=250)
    email = models.EmailField(null=True, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    pass


class Post(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text
