from rest_framework import serializers
from .models import doctors,doctors_hospitals

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctors
        fields = ('id','firstName','lastName','gender','specialist')

class DoctorsHospitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctors_hospitals
        fields = ('hospital_id','doctor_id','day','startTime','endTime')