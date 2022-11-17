from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=25, null=True)
    avatar = models.ImageField(null=True, default='/static/avatars/avatar.svg')
    bio = models.CharField(null=True, max_length=250)
    email = models.EmailField(null=True, unique=True)
    follow = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='user_follow')
    followers = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='user_followers'
    )
    has_posts = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    @property
    def num_followers(self):
        return self.followers.all().count()


class Post(models.Model):
    host = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='host')
    body = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(
        User, default=None, blank=True, related_name='liked',
    )
    bookmarked = models.ManyToManyField(User, default=None, blank=True, related_name='bookmarked')

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
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=6)

    def __str__(self):
        return self.post


BOOKMARK_CHOICES = (
    ('Bookmark', 'Bookmark'),
    ('Un_bookmark', 'Un_bookmark')
)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=BOOKMARK_CHOICES, default='Bookmark', max_length=11)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text
