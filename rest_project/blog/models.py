from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)



