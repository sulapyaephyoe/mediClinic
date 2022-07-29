from django.shortcuts import render

# Create your views here.
from doctors.serializers import DoctorsSerializer,DoctorsHospitalsSerializer
from doctors.models import doctors,doctors_hospitals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
def add_doctor(request):
    if request.method == 'POST':
        print(request.data)
        doctor_data = request.data
        doctor_serializer = DoctorsSerializer(data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data,safe=False)
    return JsonResponse(doctor_serializer.errors)
        
    # try:
    #     doctor = doctors.objects.create(
    #         firstName = request.data.firstname,
    #         lastName = request.data.lastname,
    #         gender = request.data.gender,
    #         specialist = request.data.specialist
    #     )
    #     serializer = DoctorsSerializer(data=doctor)
    #     serializer.save()
    #     return JsonResponse({'doctor': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    
    # except Exception:
    #     return JsonResponse({'error': 'Something terrible went wrong'})