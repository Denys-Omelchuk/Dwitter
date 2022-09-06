from django.contrib import admin

from base.models import Post, User
from models import User 

admin.site.register(User)
admin.site.register(Post)