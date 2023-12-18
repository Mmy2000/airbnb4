from django.urls import path
from . import views
from . import api_view


app_name = 'blog'

urlpatterns = [
    path('' , views.PostList.as_view() , name='post_list'),
    path('<slug:slug>' , views.PostDetail.as_view() , name='post_detail'),
    path('category/<str:slug>' , views.PostByCategory.as_view() , name='post_by_category'),
    path('tags/<str:slug>' , views.PostByTags.as_view() , name='post_by_tags'),

    path('api/list' , api_view.post_list_api , name='post_list_api'),
]
