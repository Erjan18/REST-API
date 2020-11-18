from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path ('',purchase_list,name='purchase'),
    path('purchase-list/',purchaseList,name='purchase-list'),
    path('purchase_create/',purchase_create,name='purchase_create'),
    path('purchase-detail/<int:pk>/',purchaseDetailList,name='purchase-detail'),
    path('update/<int:pk>/',update,name='update'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('status/',status,name=status)

]
