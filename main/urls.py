from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login', views.login, name='login'),
    path('register',views.registration, name='register'),
    path('logout', views.logoutUser, name="logout"),
    path('home',views.homeView,name='home'),
    path('user_profile',views.profile, name='user_profile'),
    path('edit-profile', views.edit_profile, name='edit-profile'),
]