from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('signup' , views.signup , name='signup'),
    path('profile/' , views.profile , name='profile'),
    path('reservation/' , views.myreservation , name='reservation'),
    path('mylisting/' , views.mylisting , name='mylisting'),

    path('profile/edit' , views.edit_profile , name='edit_profile'),
]