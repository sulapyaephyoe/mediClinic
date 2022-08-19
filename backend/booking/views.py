from django.shortcuts import render

# Create your views here.
from booking.serializers import BookingSerializer
from booking.models import booking
from django.http.response import JsonResponse 
from rest_framework.decorators import api_view

@api_view(['POST'])
def add_booking(request):
    if request.method == 'POST':
        print(request.data)
        booking_data = request.data
        booking_serializer = BookingSerializer(data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            print("hello")
            return JsonResponse(booking_serializer.data,safe=False)
        return JsonResponse(booking_serializer.errors)

@api_view(['GET'])
def get_booking(request):
    if request.method == 'GET':
        booking_data = booking.objects.all()
        print(booking_data)
        booking_serializer = BookingSerializer(booking_data,many=True)
        return JsonResponse(booking_serializer.data,safe=False)
    return JsonResponse(booking_serializer.errors)