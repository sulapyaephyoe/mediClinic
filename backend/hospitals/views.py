from django.shortcuts import render
from . serializers import HospitalSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from hospitals.models import hospitals
import folium
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage

# Create your views here.

@api_view(['POST'])
def add_hospital(request):    
    hospital = hospitals()
    hospital.name = request.data['name']
    hospital.phone = request.data['phone']
    hospital.website = request.data['website']
    hospital.type = request.data['type']
    hospital.address = request.data['address']
    hospital.latitude = request.data['latitude']
    hospital.longitude = request.data['longitude']
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
