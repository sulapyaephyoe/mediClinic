from django.urls import include,path
from . import views

urlpatterns = [
    path('add_doctor',views.add_doctor),
    path('doctorslist',views.get_doctors),
    path('add_schedule/<int:id>',views.get_doctor),
    path('add_doctor_schedule',views.add_doctor_schedule),
    path('doctor_schedule_list',views.get_doctor_schedule),
    path('doctor_schedule_list/<int:id>',views.get_one_schedule),
    path('doctor_edit/<int:id>',views.get_doctor),
    path('doctor_update/<int:id>',views.update_doctor),
    path('doctor_delete/<int:id>',views.delete_doctor),
    path('schedule_edit/<int:id>',views.edit_schedule),
]