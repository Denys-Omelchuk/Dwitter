# Generated by Django 4.0.6 on 2022-11-16 14:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_like_value_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarked',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarked', to=settings.AUTH_USER_MODEL),
        ),
    ]
