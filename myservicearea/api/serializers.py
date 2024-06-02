from .models import ServiceArea, Provider
from rest_framework_gis import serializers

class ProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provider
        fields = '__all__'
        read_only_fields = ('created', 'modified')
        

class ServiceAreaSerializer(serializers.GeoModelSerializer):
        
    class Meta:
        model = ServiceArea
        geo_field = 'area'
        fields = '__all__'
        read_only_fields = ('created', 'modified')
        
    def to_representation(self, instance):
        self.fields['provider'] = ProviderSerializer(read_only=True)
        return super().to_representation(instance)
        

class AreaLookupSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer()
    class Meta:
        model = ServiceArea
        fields = ['name', 'area', 'provider']
        