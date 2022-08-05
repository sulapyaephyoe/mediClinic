from django.urls import include,path
from . import views

urlpatterns = [
    path('add_doctor',views.add_doctor),
    path('doctorslist',views.get_doctors),
    path('add_schedule/<int:id>',views.get_doctor),
    path('add_doctor_schedule',views.add_doctor_schedule),
    path('doctor_schedule_list',views.get_doctor_schedule),
]