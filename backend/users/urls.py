from django.urls import path, re_path
from . import views

urlpatterns = [
    path('get_user/<str:name>',views.get_user_info),
    path('resetPassword',views.reset_password),
    path('updateInfo/<int:pk>',views.update_user_info),
    # re_path('get_user/(?P<name>)$',views.get_user_info)
]