from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import *


def purchase_list(request,pk):
    purchases = Purchase.objects.get(id=pk)
    context = {'purchases':purchases}
    return render(request, 'api/purchase.html', context)

@api_view(['GET'])
def purchaseList(request):
    purchases = Purchase.objects.all()
    serializers = PurchaseSerializers(purchases,many=True)
    return Response(serializers.data)

@api_view(['GET','POST'])
def purchase_create(request,pk):
    account = Account.objects.get(id=pk)
    purchase = Purchase(customer=account)
    if request.method == 'GET':
        purchase = Purchase.objects.all()
        serializers = PurchaseSerializers(purchase,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializers = PurchaseSerializers(purchase, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors)

@api_view(['GET'])
def purchaseStatus(request):
    purchase = Purchase.objects.filter(status=True)
    serializers = PurchaseSerializers(purchase,many=True)
    return Response(serializers.data)

@api_view(['PUT'])
def purchaseUpdate(request,pk):
    try:
        purchase = Purchase.objects.get(id=pk)
    except Purchase.DoesNotExist:
        return Response({'RESPONSE':'not found page'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializers = PurchaseSerializers(purchase, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'Server RESPONSE':'Purchase successfuly updates' },status=status.HTTP_200_OK)

@api_view(['DELETE'])
def purchaseDelete(request,pk):
    try:
        purchase = Purchase.objects.get(id=pk)
    except Purchase.DoesNotExist:
        return Response({'RESPONSE':'not found page'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        purchase.delete()
        return Response({'SERVER RESPONSE':'PURCHASE deletes'},status=status.HTTP_200_OK)

@api_view(['POST'])
def accountregister(request):
    if request.method == 'POST':
        serializers = AccountSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)