from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from . models import hospitals
from . serializers import HospitalSerializer

# Create your views here.

class HospitalsView(generics.ListCreateAPIView):
    queryset = hospitals.objects.all()
    serializer_class = HospitalSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = HospitalSerializer(queryset, many=True)
        return Response('success')