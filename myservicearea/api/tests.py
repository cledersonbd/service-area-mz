from django import test
from django.core.serializers import serialize
from rest_framework import status
from django.urls import reverse
from django.contrib.gis.geos import Polygon, Point
from api.models import Provider, ServiceArea
from faker import Faker
import random, json

class ProviderTests(test.TestCase):
    
    def create_provider(self):
        
        fake = Faker()
        url = reverse('provider-list')
        # creates lots of providers with fake data
        for _ in range(500):
            
            newProvider = {
                'name': fake.company(),
                'email': fake.email(),
                'phone': fake.phone_number(),
                'language': fake.language_name(),
                'currency': fake.currency_code()
            }
            
            response = self.client.post(url, newProvider, format='json')
            jsonResponse = json.loads(response.content)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            
            provider = Provider.objects.get(id=jsonResponse['id'])            
            self.assertEqual(provider.name, newProvider['name'])
            self.assertEqual(provider.email, newProvider['email'])
    
    def create_service_area(self):
        
        url = reverse('service-area-list')
        providerList = Provider.objects.all()
        # creates a miilion service areas for random providers
        for _ in range(100000):
            provider = random.choice(providerList)
            number = provider.id
            
            newServiceArea = {
                'name': 'Service Area - {number}',
                'price': random.random(),
                'area': ServiceAreaTests.randomPolygon().geojson,
                'information': 'this is a fake for Provider {number}',
                'active': False,
                'provider': number 
            }
                
            response = self.client.post(url, newServiceArea, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            
    def find_locations(self):
        lat = [-90, 90]
        lon = [-180, 180]
        
        url = reverse('lookup-list')
        providerList = Provider.objects.all()
        # search a 1000 random points
        for _ in range(1000):
            
            x = random.uniform(lat[0], lat[1])
            y = random.uniform(lon[0], lon[1])
                
            response = self.client.get(url, {'lat': x, 'lon': y})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
    
                
    def test_createProviderWithServiceArea(self):
        self.create_provider()
        self.update_provider()
        self.create_service_area()
        self.find_locations()
        
        
    def update_provider(self):
        
        faker = Faker()
        i = round(random.uniform(1, 500))
        updProvider = {
            'name': faker.company() + ' - updated',
            'email': faker.email()
        }
        
        url = reverse('provider-detail', kwargs={'pk':i})
        
        response = self.client.put(url, updProvider, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        savedProvider = Provider.objects.get(id=updProvider['id'])
        self.assertEqual(savedProvider.name, updProvider['name'])
        self.assertEqual(savedProvider.email, updProvider['email'])
        
class ServiceAreaTests(test.TestCase):        
        
    @classmethod
    def randomPolygon(cls):
        lat = [-90, 90]
        lon = [-180, 180]
        
        #  boundaries for polygon size (in degrees)
        polygon_min_size = 0.5
        polygon_max_size = 10
        
        # x,y are now our initial points for the polygon
        x = random.uniform(lat[0], lat[1])
        y = random.uniform(lon[0], lon[1])
        
        # building the polygon bottom-up, left-right
        left = Point([x, y])
        tleft = Point([x, 
                        y + random.uniform(polygon_min_size, polygon_max_size)])
        
        right = Point([x + random.uniform(polygon_min_size, polygon_max_size),
                       y])
        tright = Point([x + random.uniform(polygon_min_size, polygon_max_size),
                       y + random.uniform(polygon_min_size, polygon_max_size)])
        
        # the GIS specs states that the last and first points must be the same
        return Polygon([left, tleft, right, tright, left])
        
