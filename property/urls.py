from django.urls import path
from .views import PropertyDetail  , PropertyList , AddListing ,EditListing
from . import api_view

app_name = 'property'

urlpatterns = [
    path('',PropertyList.as_view(),name='property_list'),
    path('<slug:slug>',PropertyDetail.as_view(),name='property_detail'),
    path( 'new/',AddListing.as_view() , name='property_new' ),
    path( 'new/edit',EditListing.as_view() , name='property_edit' ),

    ## api urls ##
    path('api/list' , api_view.PropertyListApi.as_view(), name='property_api_list'),
    path('api/list/<int:pk>' , api_view.PropertyDetailApi.as_view(), name='property_api_detail')
]
