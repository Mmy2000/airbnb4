from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('signup' , views.signup , name='signup'),
    path('profile/' , views.profile , name='profile'),
    path('profile/reservation/' , views.myreservation , name='reservation'),
    path('mylisting/' , views.mylisting , name='mylisting'),
    path('profile/reservation/review/<int:property_id>/', views.submit_review , name='submit_review'),
    path('profile/edit' , views.edit_profile , name='edit_profile'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]