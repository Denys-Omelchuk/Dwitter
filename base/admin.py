from django.contrib import admin
from base.models import Post, PostComment, User, Like
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin (BaseUserAdmin):
    list_display = ("username", "email", "name",
                    "is_staff", "has_posts")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
         "fields": ("name", "email", "bio", "has_posts")}),
        (_("follow"), {"fields": ("follow",)}),
        (_("followers"), {"fields": ("followers",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Like)
