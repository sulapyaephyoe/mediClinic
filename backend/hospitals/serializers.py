from rest_framework import serializers
from . models import hospitals

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = hospitals
<<<<<<< HEAD
<<<<<<< HEAD
        fields =['id','name', 'phone','address','website','type','latitude','longitude','photo','video']
=======
        fields =['name', 'phone','address','website','type','latitude','longitude','photo','video']
>>>>>>> main
=======
        fields =['name', 'phone','address','website','type','latitude','longitude','photo','video']
>>>>>>> main
