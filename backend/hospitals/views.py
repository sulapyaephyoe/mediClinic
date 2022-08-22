from django.shortcuts import render
from . serializers import HospitalSerializer
from doctors.serializers import DoctorsSerializer,DoctorsHospitalsSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser 
from hospitals.models import hospitals
from doctors.models import doctors,doctors_hospitals
import folium
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
import geocoder

@api_view(['POST'])
def add_hospital(request):    
    hospital = hospitals()
    hospital.name = request.data['name']
    hospital.phone = request.data['phone']
    hospital.website = request.data['website']
    hospital.type = request.data['type']
    location = geocoder.osm(request.data['address'])
    print(location.address)
    hospital.address = request.data['address']
    hospital.latitude = location.lat
    hospital.longitude = location.lng
    hospital.photo = request.data['photo']
    hospital.video = request.data['video']
    hospital.save()
    return Response('success')
   
@api_view(['GET'])
def get_hospital(request):
    if request.method == 'GET':
        hospital_list = hospitals.objects.all()

        location={}
        location["lat"] = hospital_list[0].latitude
        location["lng"]= hospital_list[0].longitude
        location["address"]= hospital_list[0].address
   
        m = folium.Map(height=400,location=[12, 70], zoom_start=2,  control_scale=True)

        folium.Marker([location["lat"], location["lng"]], tooltip='Click for more',
                    popup=location["address"]).add_to(m)
        m.fit_bounds([(location["lat"],location["lng"]),(location["lat"],location["lng"])])
        m = m._repr_html_()
        serializer = HospitalSerializer(hospital_list, many=True)
        return Response({'map':m,'list':serializer.data})

@api_view(['POST'])
def get_map(request):
    if request.method == 'POST':
        hospital_data = JSONParser().parse(request)
        filted_data = hospitals.objects.filter(name=hospital_data['name'])
        for data in filted_data:
            location={}
            location["lat"] = data.latitude
            location["lng"]= data.longitude
            location["address"]= data.address  
            m = folium.Map(height=400,location=[12, 70], zoom_start=2,  control_scale=True)
        
            folium.Marker([location["lat"], location["lng"]], tooltip='Click for more',
                        popup=location["address"]).add_to(m)
            
            m.fit_bounds([(location["lat"],location["lng"]),(location["lat"],location["lng"])])
            m = m._repr_html_()

            filted_hdata = hospitals.objects.filter(name=hospital_data['name'])
            serializer = HospitalSerializer(filted_hdata, many=True)
            return Response({'map':m,'hospital_data':serializer.data})
    return Response({'map':m,'hospital_data':serializer.data})

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

        hospital_data = hospitals.objects.all()
        hospital_serializer = HospitalSerializer(hospital_data,many=True)
        finaldata.append(mydata)
        finaldata.append(hospital_serializer.data)
        return Response(finaldata)
    return Response(doctorschedule_serializer.errors)

@api_view(['POST']) 
def get_one_schedule(request,id):
    if request.method == 'POST':
        mydata = []
        finaldata = []
        doctor_schedule_data = doctors_hospitals.objects.filter(hospital_id=id).order_by('startTime')
        print(doctor_schedule_data)
        for x in doctor_schedule_data:
            print(x.doctor_id)
            doctor = doctors.objects.filter(id=x.doctor_id)
            hospital = hospitals.objects.filter(id=x.hospital_id)
            print(doctor)
            print(hospital[0].name)
            mydata.append({'firstName':doctor[0].firstName,'lastName':doctor[0].lastName,'gender':doctor[0].gender,'specialist':doctor[0].specialist,'day':x.day,
            'startTime':x.startTime.strftime('%H:%M'),'endTime':x.endTime.strftime('%H:%M')})
        # mydata = [{'name':doctor_name[0].firstName, 'specialist':doctor_name[0].specialist},{'name':'JJJ', 'specialist':'special'}]
        doctorschedule_serializer = DoctorsHospitalsSerializer(doctor_schedule_data,many=True)

        hospital_data = hospitals.objects.all()
        hospital_serializer = HospitalSerializer(hospital_data,many=True)
        finaldata.append(mydata)
        finaldata.append(hospital_serializer.data)
        return Response(finaldata)
    return Response(doctorschedule_serializer.errors)

#Show Hospital List     
@api_view(['GET']) 
def get_hospitals(request):
    if request.method == 'GET':
        hospital_data = hospitals.objects.filter()[:3]
        hospital_serializer = HospitalSerializer(hospital_data,many=True)
        return JsonResponse(hospital_serializer.data,safe=False)
    return JsonResponse(hospital_serializer.errors)