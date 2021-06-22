from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ApiTestCase(APITestCase):
    def test_errors_city_missing(self):
        """
        Make sure returns the right error data
        """
        url = reverse('locations-detail', args=(' ',))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertEqual(data['message'], 'No matching location found.')

    def test_success(self):
        """
        Make sure returns the right error data
        """
        url = reverse('locations-detail', args=('London',))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['maximum'])
        self.assertTrue(data['average'])
        self.assertTrue(data['minimum'])
        self.assertTrue(data['median'])
