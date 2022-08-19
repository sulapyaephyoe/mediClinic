from rest_framework import serializers
from .models import booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ('id','patient','email','phone','doctortype','datetime','fee','service')