from http.client import HTTPResponse, ResponseNotReady
from django import http
from django.shortcuts import render
from rest_framework.decorators import api_view
from . import serializers
from .models import Articles
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def read_post(request):
    blogs = Articles.objects.all()
    # print(blogs)
    if blogs:
        # print('CHECK-OK')
        result = serializers.ArticleSerializer(blogs, many = True)
        # print(result.data)
        return Response(result.data)
    else:
        return Response(data = {"message" : "Error!"}, status = status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def read_one_post(request, idx):
    blogs = Articles.objects.get(id = idx)
    # print(blogs)
    if blogs:
        # print('CHECK-OK')
        result = serializers.ArticleSerializer(blogs)
        # print(result.data)
        return Response(result.data)
    else:
        return Response(data = {"message" : "Error!"}, status = status.HTTP_404_NOT_FOUND)
        

@api_view(['POST'])
def create_blog(request):
    serializer = serializers.BlogSerializer(data = request.data)
    if Articles.objects.filter(**request.data).exists():
        return Response(data = {"message" : "Data Already Exists"}, status = status.HTTP_204_NO_CONTENT)
    
    if serializer.is_valid():
        serializer.save()
        return Response(data = serializer.data)
    else:
        return Response(data = {"message" : "NOT A VALID TYPE"}, status = status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_blog(request, idx):
    blog = Articles.objects.get(id = idx)
    if blog:
        article = serializers.ArticleSerializer(instance = blog, data = request.data)
        if article.is_valid():
            article.save()
            return Response(data = article.data)
    else:
        return Response(date = {"message" : "Data Not Found"}, status = status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_blog(request, idx):
    blog = Articles.objects.get(id = idx)
    
    if blog:
        blog.delete()
        return Response(data = {"message" : "Deleted Successfully"}, status = status.HTTP_200_OK)
    else:
        return Response(date = {"message" : "Found Nothing to Delete"}, status = status.HTTP_404_NOT_FOUND)