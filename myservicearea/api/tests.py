from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Provider

class ProviderTests(APITestCase):
    
    def test_create_provider(self):
        newProvider = {
            'name': 'Provider 1',
            'email': 'email@provider1.com'
        }
        
        url = reverse('provider-list')
        
        response = self.client.post(url, newProvider, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Provider.objects.get().name, newProvider['name'])
        self.assertEqual(Provider.objects.get().email, newProvider['email'])
        
        
    def test_update_provider(self):
        updProvider = {
            'id': 1,
            'name': 'Provider 1 - updated',
            'email': 'email@provider1-upd.com'
        }
        url = reverse('provider-list')
        response = self.client.post(url, updProvider, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        savedProvider = Provider.objects.get(id=updProvider['id'])
        
        self.assertEqual(savedProvider.name, updProvider['name'])
        self.assertEqual(savedProvider.email, updProvider['email'])
        