from django.shortcuts import render
from base.models import Post


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/home.html', context)
