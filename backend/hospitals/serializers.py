from rest_framework import serializers
from . models import hospitals

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = hospitals
        fields =['id','name', 'phone','address','website','type','latitude','longitude','photo','video']
