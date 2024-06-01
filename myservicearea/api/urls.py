from django.urls import path
from . import views


urlpatterns = [
    path('provider', 
         views.ProviderList.as_view(), 
         name='provider-list'),
    path('provider/<int:pk>', 
         views.ProviderDetail.as_view(), 
         name='provider-list2'),
    path('servicearea', 
         views.ServiceAreaList.as_view(), 
         name='service-area-list'),
    path('lookup', 
         views.LookupList.as_view(), 
         name='lookup-list'),
]

