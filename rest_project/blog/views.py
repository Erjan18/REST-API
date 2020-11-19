from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def post_list(request):
    post = Post.objects.all()
    serializers = PostSerializer(post,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def post_create(request,pk):
    blog = Post.objects.get(id=pk)
    post = Post(blog=blog)
    if request.method == 'POST':
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

