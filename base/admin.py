from django.contrib import admin
from base.models import Post, PostComment, User
 

admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostComment)
