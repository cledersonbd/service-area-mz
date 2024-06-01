from .models import ServiceArea, Provider
from rest_framework_gis import serializers

class ProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provider
        fields = '__all__'
        

class ServiceAreaSerializer(serializers.GeoModelSerializer):
    
    class Meta:
        model = ServiceArea
        geo_field = 'area'
        fields = '__all__'


