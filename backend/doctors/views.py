from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from doctors.serializers import DoctorsSerializer,DoctorsHospitalsSerializer
from doctors.models import doctors,doctors_hospitals
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse


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
#Show Doctor List     
@api_view(['GET']) 
def get_doctors(request):
    if request.method == 'GET':
        doctor_data = doctors.objects.all()
        print(doctor_data)
        doctor_serializer = DoctorsSerializer(doctor_data,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)
    return JsonResponse(doctor_serializer.errors)

#For Adding Schedule
@api_view(['GET'])
def get_doctor(request,id):
    if request.method == 'GET':
        doctor_data = doctors.objects.get(id=id)
        print(doctor_data)
        doctor_serializer = DoctorsSerializer(doctor_data)
        return JsonResponse(doctor_serializer.data,safe=False)
    return JsonResponse(doctor_serializer.errors)

#Create Doctor Schedule
@api_view(['POST'])
def add_doctor_schedule(request):
    if request.method == 'POST':
        print(request.data)
        schedule_data = request.data
        for i in schedule_data:
            print(i)        
            schedule_serializer = DoctorsHospitalsSerializer(data=i)
            if schedule_serializer.is_valid():
                schedule_serializer.save()
                
        return JsonResponse(schedule_serializer.data,safe=False)
    return JsonResponse(schedule_serializer.errors)

#Show Doctor Schedule
@api_view(['GET']) 
def get_doctor_schedule(request):
    if request.method == 'GET':
        doctor_schedule_data = doctors_hospitals.objects.all()
        print(doctor_schedule_data)
        print(doctor_schedule_data[0].doctor_id)
        doctor_name = doctors.objects.filter(id=doctor_schedule_data[0].doctor_id)
        print(doctor_name[0].firstName)
        doctor_schedule_data[0].doctor_id = doctor_name[0].firstName
        mydata = [{'name':doctor_name[0].firstName, 'specialist':doctor_name[0].specialist},{'name':'JJJ', 'specialist':'special'}]
        doctorschedule_serializer = DoctorsHospitalsSerializer(doctor_schedule_data,many=True)
        return JsonResponse(mydata,safe=False)
    return JsonResponse(doctorschedule_serializer.errors)

