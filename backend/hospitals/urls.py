from django.urls import path 
from . import views

urlpatterns = [
    path('add_hospital',views.add_hospital),
    path('get_hospital',views.get_hospital),
    path('get_map',views.get_map),
    path('doctor_schedule_list',views.get_doctor_schedule),
    path('doctor_schedule_list/<int:id>',views.get_one_schedule),
    path('hospitalslist',views.get_hospitals),
]