from django.urls import path 
from . import views

urlpatterns = [
    path('add_hospital',views.add_hospital),
    path('get_hospital',views.get_hospital),
    path('get_map',views.get_map),
]