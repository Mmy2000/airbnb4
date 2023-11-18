from django.urls import path
from .views import PropertyDetail  , PropertyList , AddListing 

app_name = 'property'

urlpatterns = [
    path('',PropertyList.as_view(),name='property_list'),
    path('<slug:slug>',PropertyDetail.as_view(),name='property_detail'),
    path( 'new/',AddListing.as_view() , name='property_new' ),
]
