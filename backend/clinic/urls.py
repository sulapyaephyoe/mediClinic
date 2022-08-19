from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/login/', include('dj_rest_auth.registration.urls')),
    path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('users/', include('users.urls')),
    path('doctors/', include('doctors.urls')),
    path('hospitals/', include('hospitals.urls')),
    path('booking/', include('booking.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
