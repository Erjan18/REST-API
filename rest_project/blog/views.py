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

@api_view(['GET'])
def blog_list(request):
    blog = Blog.objects.all()
    serializers = BlogSerializer(blog,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def blog_create(request):
    if request.method == 'POST':
        serializers = BlogSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def post_view(request,pk):
    if request.method == "GET":
        posts = Post.objects.filter(blog_id=pk)
        serializers = PostSerializer(posts,many=True)
        return Response(serializers.data)
    if request.method == 'POST':
        try:
            blog = Blog.objects.get(id=pk)
            post = Post(blog=blog)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializers = PostSerializer(post,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors)

@api_view(['PUT'])
def blog_update(request,pk):
    if request.method == 'PUT':
        try:
            blog = Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return Response({'RESPONSE':'not found page'}, status=status.HTTP_404_NOT_FOUND)
        serializers = BlogSerializer(blog, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'Server RESPONSE': 'Blog successfuly updates'}, status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def post_update(request,blog_id,post_id):
    if request.method == 'PUT':
            blog = Blog.objects.get(id=blog_id)
            post = Post.objects.get(id=post_id)
            serializers = PostSerializer(post, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_200_OK)
            return Response(serializers.errors)

@api_view(['DELETE'])
def blog_delete(request,pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'DELETE':
      blog.delete()
    return Response({'Server RESPONSE': 'Blog successfuly deleted'})

@api_view(['DELETE'])
def post_delete(request,blog_id,post_id):
    blog = Blog.objects.get(id=blog_id)
    post = Post.objects.get(id=post_id)
    if request.method == 'DELETE':
      post.delete()
    return Response({'Server RESPONSE': 'Post successfuly deleted'})