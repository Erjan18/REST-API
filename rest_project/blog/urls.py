from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('blog_create/',blog_create,name='blog_create'),
    path('post_list/',post_list,name='post_list'),
    path('blog_list/',blog_list,name='blog_list'),
    path('post_view/<int:pk>/',post_view,name='post_view'),
    path('blog_update/',blog_update,name='blog_update'),
    path('blog_update/<int:pk>/',blog_update,name='blog_update'),
    path('post_view/<int:blog_id>/post_update/<int:post_id>/',post_update,name='post_update'),
    path('blog_delete/<int:pk>/',blog_delete,name='blog_delete'),
    path('post_view/<int:blog_id>/post_delete/<int:post_id>/',post_delete,name='post_delete'),

]