from django.urls import include,path
from . import views

urlpatterns = [
    path('add_doctor',views.add_doctor)
]