from django.db import models
from djgeojson.fields import PolygonField


class Provider(models.Model):
    name = models.CharField(max_length=100, blank=False, default = '')
    email = models.EmailField(max_length=100, blank=False, default = '')
    phone = models.CharField(max_length=100, blank=False, default = '') 
    language = models.CharField(max_length=100, blank=False, default = '')
    currency = models.CharField(max_length=3, blank=False, default = '')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'providers'


class ServiceArea(models.Model):
    name = models.CharField(max_length=100, blank=False, default = '')
    price = models.DecimalField(blank=False, default = '')
    polygon = PolygonField()
    information = models.CharField(max_length=100, blank=False, default = '')
    active = models.BooleanField()
    provider = models.ForeignKey(Provider, 
                                 related_name='areas', 
                                 on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'service_areas'
        
        