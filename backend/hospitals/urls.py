from django.urls import path 
from . views import HospitalsView

urlpatterns = [
    path('hospital/', HospitalsView.as_view(), name='posts_view')
]