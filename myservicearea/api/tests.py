from django.test import TestCase
from django.core.serializers import serialize
from rest_framework import test, status
from django.urls import reverse
from django.contrib.gis.geos import Polygon
from api.models import Provider
import json

class ProviderTests(test.APITestCase):
    
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
        
class ServiceAreaTests(test.APITestCase):
    
    def test_create_service_area(self):
        ext_coords = ((0, 0), (0, 1), (1, 1), (1, 0), (0, 0))
        int_coords = ((0.4, 0.4), (0.4, 0.6), (0.6, 0.6), (0.6, 0.4), (0.4, 0.4))
        
        newServiceArea = {
            'name': 'Service Area test 1',
            'price': 15.45,
            'area': Polygon(ext_coords, int_coords),
            'information': 'this is a fake',
            'active': True,
            'provider': 1
        }
        
        
        
        # data = serialize('geojson', newServiceArea, geometry_field='area')
        f = open('mydata.txt', 'w')
        f.write(json.dumps(serialize('geojson', newServiceArea, geometry_field='area')))
        f.close()
        
        url = reverse('service-area-list')
        response = self.client.post(url, data=newServiceArea, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response)
        
        