from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from . models import Posts
from . serializers import PostSerializer

class PostsView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        print('Reached into post function ----------\n ', request.data)
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
        
