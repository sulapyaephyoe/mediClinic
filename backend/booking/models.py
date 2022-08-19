
from django.db import models

# Create your models here.\
class booking(models.Model):
    patient = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=100,blank=True, null=True)
    doctortype = models.CharField(max_length=100,blank=True, null=True)
    datetime = models.DateTimeField('%Y-%m-%d %H:%M:%S',blank=True, null=True)
    fee = models.IntegerField(blank=True, null=True)
    service = models.CharField(max_length=100,blank=True, null=True)
