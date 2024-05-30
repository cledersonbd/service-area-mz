from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import ServiceArea, Provider
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderView(APIView):
    
    def get(self, request, format=None):
        result = Provider.objects.all()
        serializer = ProviderSerializer(result, many=True)        
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProviderSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
    @csrf_exempt
    def provider_detail(request, id):
                
        try:
            result = Provider.objects.get(id=id)
        except Provider.DoesNotExist:
            return HttpResponse(status=404)
        
        return JsonResponse(ProviderSerializer(result).data, safe=False)


class ServiceAreaList(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    