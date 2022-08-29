from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.contrib.auth.models import User
from . serializers import UserSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from users.utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

import random

@api_view(['POST'])
def set_user_group(request):
    if request.method == 'POST':
        user_data = request.data
        my_group = Group.objects.get(name='Guests')
        my_group.user_set.add(user_data)
    return JsonResponse(user_data)

@api_view(['GET'])
def get_user_info(request,name):
    if request.method == 'GET':
        u = User.objects.get(username=name)
        user_serializer = UserSerializer(u)
    return JsonResponse(user_serializer.data)

@api_view(['PUT'])
def update_user_info(request,pk):
    uid = User.objects.get(id=pk)
    user_data = JSONParser().parse(request) 
    user_data['password'] = make_password(user_data['password'])
    user_serializer = UserSerializer(uid, data=user_data) 
    if user_serializer.is_valid(): 
        user_serializer.save() 
        return JsonResponse(user_serializer.data) 
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def reset_password(request):
    if request.method == 'POST':
        email = request.data['email']
        user = User.objects.get(email=email)
        user_data = UserSerializer(user).data
        code = password_mail_send(email, user)
        # my_group = Group.objects.get(name='Guests')
        # my_group.user_set.add(user_data)
        user_data["code"] = code
    return JsonResponse(user_data)

def password_mail_send(email, user):
    data_bytes = email.encode("utf-8")
    uidb64 = urlsafe_base64_encode(data_bytes)
    token = random.randint(100000,999999)

    rel_link = "http://localhost:8080/users/forgetPassword"
    email_body = 'From Mediclinc OJT \n Please use the following code to reset your password '+ str(token)
    data = {'email_subject': 'Reset your passsword', 'email_body': email_body, 'to_email': user.email}
    Util.send_email(data)
    return str(token)

@api_view(['POST'])
def contact_mail_send(request):
    message = 'Name: '+ request.data['name'] + '\n Email: ' + request.data['email'] + '\n Message: ' + request.data['message']
    data = {'email_subject':'Contact Inqury from '+request.data['email'],'to_email': 'ecctester2222@gmail.com','email_body':message}
    Util.send_email(data)
    return Response('success')
