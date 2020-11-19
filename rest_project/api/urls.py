from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path ('',purchase_list,name='purchase'),
    path('purchase-list/',purchaseList,name='purchase-list'),
    path('purchase_create/<int:pk>/',purchase_create,name='purchase_create'),
    # path('purchase-detail/<int:pk>/',purchaseDetailList,name='purchase-detail'),
    path('purchaseUpdate/<int:pk>/',purchaseUpdate,name='update'),
    # path('delete/<int:pk>/',delete,name='delete'),
    path('purchaseStatus/',purchaseStatus,name='status'),
    path('purchaseDelete/<int:pk>/',purchaseDelete,name='putrchaseDelete'),
    path('accountregister/',accountregister,name='accountregister')

]
