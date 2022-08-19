from django.urls import path 
from . import views

urlpatterns = [
    path('get_specialists',views.get_specialists),
    path('get_schedule_data/<str:sname>',views.get_schedule_data),
]