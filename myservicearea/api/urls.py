from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_root),
    path('provider', 
         views.ProviderList.as_view(), 
         name='provider-list'),
    path('provider/<int:pk>', 
         views.ProviderDetail.as_view(), 
         name='provider-detail'),
    path('servicearea', 
         views.ServiceAreaList.as_view(), 
         name='service-area-list'),
    path('servicearea/<int:pk>', 
         views.ServiceAreaDetail.as_view(), 
         name='service-area-detail'),
    path('lookup', 
         views.LookupList.as_view(), 
         name='lookup-list'),
]

