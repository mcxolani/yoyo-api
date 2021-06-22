from django.urls import path, include
from rest_framework import routers
from .views import WeatherViewSet

router = routers.DefaultRouter()
router.register('locations', WeatherViewSet, basename='locations')

# /api/locations/{city}/?days={number_of_days}
urlpatterns = [
    path('', include(router.urls))
]