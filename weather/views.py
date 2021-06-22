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

        data = response.json()['forecast']['forecastday']
        avg_list_per_day = [d['day']['avgtemp_c'] for d in data]
        median = self.calculate_mean(avg_list_per_day)
        average = self.calculate_avg(avg_list_per_day)
        maximum = self.get_max(avg_list_per_day)
        minimum = self.get_min(avg_list_per_day)
        return True, {'average': average, 'median': median, 'maximum': maximum, "minimum": minimum}

    def calculate_mean(self, temps):
        n = len(temps)
        temps.sort()
        
        if n % 2 == 0:
            median1 = temps[n//2]
            median2 = temps[n//2 - 1]
            median = (median1 + median2)/2
        else:
            median = temps[n//2]
        return median

    def calculate_avg(self, temps):
        n = len(temps)
        temps_sum = sum(temps)
        return temps_sum / n

    def get_max(self, temps):
        return max(temps)

    def get_min(self, temps):
        return min(temps)