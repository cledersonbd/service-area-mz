from .models import ServiceArea, Provider
from rest_framework_gis import serializers

class ProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provider
        fields = '__all__'
        

class ServiceAreaSerializer(serializers.GeoModelSerializer):
    provider = ProviderSerializer()
    
    class Meta:
        model = ServiceArea
        geo_field = 'area'
        fields = '__all__'

class AreaLookupSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer()
    class Meta:
        model = ServiceArea
        fields = ['name', 'area', 'provider']