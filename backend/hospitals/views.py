from django.shortcuts import render
from . serializers import HospitalSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from hospitals.models import hospitals
import folium
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def add_hospital(request):
    if request.method == 'POST':
        hospital_data = JSONParser().parse(request)
        hospital_serializer = HospitalSerializer(data=hospital_data)
        if hospital_serializer.is_valid():
            hospital_serializer.save()
            return JsonResponse(hospital_serializer.data,safe=False)
    return JsonResponse(hospital_serializer.errors)

@api_view(['GET'])
def get_hospital(request):
    if request.method == 'GET':
        list = hospitals.objects.all()
        hospital_list = hospitals.objects.all()

        location={}
        location["lat"] = list[0].latitude
        location["lng"]= list[0].longitude
        location["address"]= list[0].address   
   

        m = folium.Map(width=800, height=400,location=[12, 70], zoom_start=2,  control_scale=True)

        folium.Marker([location["lat"], location["lng"]], tooltip='Click for more',
                    popup=location["address"]).add_to(m)
        m.fit_bounds([(location["lat"],location["lng"]),(location["lat"],location["lng"])])
        m = m._repr_html_()
        # print(m)
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
            m = folium.Map(width=800, height=400,location=[12, 70], zoom_start=2,  control_scale=True)
        
            folium.Marker([location["lat"], location["lng"]], tooltip='Click for more',
                        popup=location["address"]).add_to(m)
            
            m.fit_bounds([(location["lat"],location["lng"]),(location["lat"],location["lng"])])
            m = m._repr_html_()

            filted_hdata = hospitals.objects.filter(name=hospital_data['name'])
            serializer = HospitalSerializer(filted_hdata, many=True)
           
            return Response({'map':m,'hospital_data':serializer.data})
    return Response({'map':m,'hospital_data':serializer.data})