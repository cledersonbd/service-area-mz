from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView
from rest_framework import status, mixins, generics
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from django.contrib.gis.geos import Point
from .models import ServiceArea, Provider
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    
class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaList(APIView):
    
    def get(self, request, id=None):
        
        if id: 
            try:                
                result = ServiceArea.objects.get(id=id)
            except ServiceArea.DoesNotExist:
                return HttpResponse(status=404)
            
            return JsonResponse(ServiceAreaSerializer(result).data, safe=False)
        
        return JsonResponse(
            ServiceAreaSerializer(ServiceArea.objects.all(), many=True).data, 
            safe=False)
        
    def post(self, request):
        
        print(request)
        data = JSONParser().parse(request)
        serializer = ServiceAreaSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
    
class LookupList(APIView):
    
    def get(self, request):
        
        point = Point(
            (float(request.query_params['lat']), 
             float(request.query_params['lon']))
        )
        
        result = ServiceAreaSerializer(
            ServiceArea.objects.filter(area__contains=point), many=True)
        
        return JsonResponse(result.data, safe=False)
        # return JsonResponse({
        #     'lat': request.query_params['lat'], 
        #     'lon': request.query_params['lon']
        #     }, safe=False)
    