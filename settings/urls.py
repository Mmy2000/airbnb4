from django.urls import path
from . views import home , home_search , category_filter , contact , news_letters_subscribe , place_filter

app_name = 'settings'

urlpatterns = [
    path('', home ,name = 'home'),
    path('search' , home_search , name = 'home_search'),
    path( 'contact',contact , name='contact' ),
    path('newsletter/' , news_letters_subscribe , name = 'newsletter'),
    path('category/<slug:category>' , category_filter , name = 'category_filter'),
    path('place/<slug:place>' , place_filter , name = 'place_filter'),
]
