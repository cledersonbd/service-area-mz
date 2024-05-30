from rest_framework import serializers
from .models import ServiceArea, Provider

class ProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provider
        fields = '__all__'
        

class ServiceAreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceArea
        fields = '__all__'
        

