from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView
from rest_framework import status, generics, permissions
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from django.contrib.gis.geos import Point
from .models import ServiceArea, Provider
from .serializers import ProviderSerializer, ServiceAreaSerializer, AreaLookupSerializer
from .permissions import IsOwnerOrReadOnly


class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly]
    
class ServiceAreaList(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly]
    
class LookupList(APIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        
        point = Point(
            (float(request.query_params['lat']), 
             float(request.query_params['lon']))
        )
        # perform 2 polkygon searches - within and intersection
        intersects = AreaLookupSerializer(
            ServiceArea.objects.filter(area__intersects=point), many=True)
        within = AreaLookupSerializer(
            ServiceArea.objects.filter(area__within=point), many=True)
        
        result = intersects.data
        result.extend(within.data)
        
        # TODO improve the fail case (faster method)
        if len(result) > 0:
            return JsonResponse(result, safe=False)
        
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    