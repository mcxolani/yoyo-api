from rest_framework import viewsets
from rest_framework.response import Response

class WeatherViewSet(viewsets.ViewSet):
    lookup_field = 'city'

    def retrieve(self, request, city=None):
        days = request.GET.get('days', '1')
        return Response({})