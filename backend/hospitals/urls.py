from django.urls import path 
from . import views

urlpatterns = [
    path('add_hospital',views.add_hospital)
]