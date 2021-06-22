import requests
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response

API_KEY = settings.WEATHER_API_KEY

class WeatherViewSet(viewsets.ViewSet):
    lookup_field = 'city'

    def retrieve(self, request, city=None):
        days = request.GET.get('days', '1')
        success, data = self.get_weather_data(city=city, days=days)
        if not success:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)

    def get_weather_data(self, city, days):
        response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}&aqi=no&alerts=no")
        if response.status_code == 400:
            data = response.json()
            return False, data['error']

        return True, {}

    def calculate_mean(self):
        return 1

    def calculate_avg(self):
        return 1

    def get_max(self):
        return 1

    def get_min(self):
        return 1