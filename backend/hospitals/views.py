from django.shortcuts import render
from . serializers import HospitalSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

@api_view(['POST'])
def add_hospital(request):
    if request.method == 'POST':
        hospital_data = JSONParser().parse(request)
        print('checking hospital data: ', hospital_data)
        hospital_serializer = HospitalSerializer(data=hospital_data)
        if hospital_serializer.is_valid():
            hospital_serializer.save()
            return JsonResponse(hospital_serializer.data,safe=False)
    return JsonResponse(hospital_serializer.errors)