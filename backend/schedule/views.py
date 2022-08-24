from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse,HttpResponse
from rest_framework.response import Response

from doctors.serializers import DoctorsSerializer,DoctorsHospitalsSerializer
from doctors.models import doctors,doctors_hospitals
from hospitals.models import hospitals
from hospitals.serializers import HospitalSerializer
from django.db.models import Subquery, OuterRef, Q
from itertools import chain
from django.core import serializers

@api_view(['GET']) 
def get_specialists(request):
    if request.method == 'GET':
        doctor_data = doctors.objects.values('specialist').distinct()
        return Response(doctor_data)
    return Response({"errors":'error returned'})

@api_view(['GET'])
def get_schedule_data(request,sname):
    if request.method == 'GET':
        data = {}
        doctor_query = doctors.objects.filter(specialist=sname)
        join_data = doctors_hospitals.objects.filter(doctor_id__in=doctor_query).order_by('startTime') 

        doctor_data = doctors.objects.filter(id__in = (join_data).values('doctor_id'))
        hospital_data = hospitals.objects.filter(id__in = (join_data).values('hospital_id'))
        data = {
            'join_data': DoctorsHospitalsSerializer(join_data,many=True).data,
            'doctor_data': DoctorsSerializer(doctor_data,many=True).data,
            'hospital_data': HospitalSerializer(hospital_data,many=True).data
        }
        return JsonResponse(data,safe=False)
    return JsonResponse({"error":"error"})
