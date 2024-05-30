from django.urls import path
from . import views


urlpatterns = [
    path('provider', 
         views.ProviderView.as_view(), 
         name='provider-list'),
    path('provider/<int:id>', 
         views.ProviderView.provider_detail, 
         name='provider-list2'),
    path('servicearea/', 
         views.ServiceAreaList.as_view(), 
         name='service-area-list'),
    
]

