from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response


def purchase_list(request,pk):
    purchases = Purchase.objects.get(id=pk)
    context = {'purchases':purchases}
    return render(request, 'api/purchase.html', context)

@api_view(['GET'])
def purchaseList(request):
    purchases = Purchase.objects.all()
    serializers = PurchaseSerializers(purchases,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def purchase_create(request):
    serializers = PurchaseSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
def purchaseDetailList(request,pk):
    purchase = Purchase.objects.get(id=pk)
    serializers = PurchaseSerializers(purchase,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def update(request,pk):
    purchase = Purchase.objects.get(id=pk)
    serializers = PurchaseSerializers(instance=purchase,data=request.data,many=False)
    if serializers.is_valid():
        serializers.save()
        return Response(request.data)

@api_view(['POST'])
def delete(request,pk):
    purchase = Purchase.objects.get(id=pk)
    serializers = PurchaseSerializers(instance=purchase,data=request.data,many=False)
    if serializers.is_valid():
        purchase.delete()
        return Response(request.data)

@api_view(['POST'])
def status(request):
    purchase = Purchase.objects.filter(status=True)
    serializers = PurchaseSerializers(instance=purchase,data=request.data,many=True)
    if Purchase.status == True:
        purchase.save()
        return Response(serializers.data)

