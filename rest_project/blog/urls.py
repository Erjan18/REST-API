from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('post_create/<int:pk>/',post_create,name='post_create'),
    path('post_list/',post_list,name='post_list'),

]