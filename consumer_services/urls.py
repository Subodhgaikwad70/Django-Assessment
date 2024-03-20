from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-service-request/', views.submit_service_request, name='submit_service_request'),
    path('track-service-request/', views.track_service_request, name='track_service_request'),
    path('track-service-request/<int:request_id>/', views.track_service_request, name='track_service_request_with_id'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    # Other URL patterns
]
