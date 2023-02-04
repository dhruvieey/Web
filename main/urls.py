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
    path('guess_the_word',views.guess_the_word,name='guess_the_word'),
    path('multiplication_game',views.multiplication_game,name='multiplication_game'),
    path('breakfast',views.Breakfast),
    path('lunch',views.Lunch),
    path('dinner',views.Dinner),
    path('arithmetic',views.arithmetic),
    path('level1',views.level1),
    path('level2',views.level2),
    path('level3',views.level3),
    path('levels',views.levels),
    path('voice',views.save_recorded_audio,name='voice'),
    path('maze',views.maze),
    path('crossword',views.crossword)
]