from django.contrib import admin
from base.models import Post, PostComment, User, Like
 

admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Like)
