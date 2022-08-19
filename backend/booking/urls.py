from django.urls import include,path
from . import views

urlpatterns = [
    path('add_booking',views.add_booking),
    path('bookinglist',views.get_booking),
]