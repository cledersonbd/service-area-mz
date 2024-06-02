from django.db import models
from django.contrib.gis.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=50) 
    language = models.CharField(max_length=100, blank=False)
    currency = models.CharField(max_length=3, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', related_name='providers', 
                             on_delete=models.CASCADE, default=1)
    
    class Meta:
        db_table = 'providers'


class ServiceArea(models.Model):
    name = models.CharField(max_length=100, blank=False, default = '')
    price = models.FloatField()
    area = models.PolygonField(default=None)
    active = models.BooleanField()
    provider = models.ForeignKey(Provider, 
                                 related_name='areas', 
                                 on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', related_name='areas', 
                             on_delete=models.CASCADE, default=1)
    
    class Meta:
        db_table = 'service_areas'
        
        