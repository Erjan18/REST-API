from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
class Purchase(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=False,null=True)
    customer = models.ForeignKey('Account',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class Account(AbstractBaseUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.name + ' ' + self.last_name
