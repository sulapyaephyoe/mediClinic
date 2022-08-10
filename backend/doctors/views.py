from django.shortcuts import render

# Create your views here.
from doctors.serializers import DoctorsSerializer,DoctorsHospitalsSerializer
from doctors.models import doctors,doctors_hospitals
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
        mydata = []
        finaldata = []
        doctor_schedule_data = doctors_hospitals.objects.filter(doctor_id=3).order_by('startTime')
        print(doctor_schedule_data)
        for x in doctor_schedule_data:
            print(x.doctor_id)
            doctor = doctors.objects.filter(id=x.doctor_id)
            print(doctor)
            mydata.append({'hospital_name':'Victoria Hospital','name':doctor[0].firstName,'specialist':doctor[0].specialist,'day':x.day,
            'startTime':x.startTime.strftime('%H:%M'),'endTime':x.endTime.strftime('%H:%M')})
        # mydata = [{'name':doctor_name[0].firstName, 'specialist':doctor_name[0].specialist},{'name':'JJJ', 'specialist':'special'}]
        doctorschedule_serializer = DoctorsHospitalsSerializer(doctor_schedule_data,many=True)

        doctor_data = doctors.objects.all()
        doctor_serializer = DoctorsSerializer(doctor_data,many=True)
        finaldata.append(mydata)
        finaldata.append(doctor_serializer.data)
        return JsonResponse(finaldata,safe=False)
    return JsonResponse(doctorschedule_serializer.errors)

@api_view(['POST']) 
def get_one_schedule(request,id):
    if request.method == 'POST':
        mydata = []
        finaldata = []
        doctor_schedule_data = doctors_hospitals.objects.filter(doctor_id=id).order_by('startTime')
        print(doctor_schedule_data)
        for x in doctor_schedule_data:
            print(x.doctor_id)
            doctor = doctors.objects.filter(id=x.doctor_id)
            print(doctor)
            mydata.append({'hospital_name':'Victoria Hospital','name':doctor[0].firstName+doctor[0].lastName,'specialist':doctor[0].specialist,'day':x.day,
            'startTime':x.startTime.strftime('%H:%M'),'endTime':x.endTime.strftime('%H:%M')})
        # mydata = [{'name':doctor_name[0].firstName, 'specialist':doctor_name[0].specialist},{'name':'JJJ', 'specialist':'special'}]
        doctorschedule_serializer = DoctorsHospitalsSerializer(doctor_schedule_data,many=True)

        doctor_data = doctors.objects.all()
        doctor_serializer = DoctorsSerializer(doctor_data,many=True)
        finaldata.append(mydata)
        finaldata.append(doctor_serializer.data)
        return JsonResponse(finaldata,safe=False)
    return JsonResponse(doctorschedule_serializer.errors)

@api_view(['POST'])
def update_doctor(request,id):
    if request.method == 'POST':
        print(request.data)
        doctor = doctors.objects.get(id = id)
        print(doctor)
        doctor_data = request.data
        doctor_serializer = DoctorsSerializer(instance=doctor, data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data,safe=False)
    return JsonResponse(doctor_serializer.errors)
