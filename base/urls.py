from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('like/', views.like_post, name='like_post'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name="register")
]


