from django.shortcuts import render
from rest_framework.response import responses
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
