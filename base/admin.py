from django.contrib import admin

from base.models import Post, PostComment, User
from models import User 

admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostComment)
