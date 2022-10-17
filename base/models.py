from email.policy import default
from pyexpat import model
from random import choices
from tkinter import CASCADE
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
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='host')
    body = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=10)

    def __str__(self):
        return self.post


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text
