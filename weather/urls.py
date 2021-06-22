from django.urls import path, include
from rest_framework import routers
from .views import WeatherViewSet

router = routers.DefaultRouter()
router.register('locations', WeatherViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls))
]