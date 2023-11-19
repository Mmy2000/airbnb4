from django.http import JsonResponse
from django.shortcuts import render
from property.models import Property , Place , Category , PropertyReview
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from django.contrib.auth.models import User
from .models import NewsLitter
from .models import  Info
from django.core.mail import send_mail
from django.conf import settings
from .tasks import send_mail_task



def home(request,):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()

    resturant_list = Property.objects.filter(category__name = 'restaurant')[:4]
    hotel_list = Property.objects.filter(category__name = 'hotels')[:4]
    places_list = Property.objects.filter(category__name = 'Places')[:4]
    recent_post = Post.objects.all()[:4]

    users_count = User.objects.all().count()
    resturant_count = Property.objects.filter(category__name = 'restaurant').count()
    hotel_count = Property.objects.filter(category__name = 'hotels').count()
    places_count = Property.objects.filter(category__name = 'Places').count()
    propertys = Property.objects.all()
    for property in propertys:
        reviews = PropertyReview.objects.filter( property_id=property.id)




    return render(request, 'settings/home.html',{
        'places' : places,
        'category' : category,
        'resturant_list':resturant_list,
        'hotel_list':hotel_list,
        'places_list':places_list,
        'recent_post' : recent_post,
        'users_count' : users_count,
        'places_count' : places_count,
        'hotel_count' : hotel_count,
        'resturant_count' : resturant_count,
        'reviews':reviews,
        'propertys':propertys,
    })

def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property_list = Property.objects.filter(
        Q(name__icontains = name) &
        Q(place__name__icontains = place)
    )
    return render(request , 'settings/home_search.html' , {'property_list':property_list})

def category_filter(request , category):
    category = Category.objects.get(name = category)
    property_list = Property.objects.filter(category=category)
    return render(request , 'settings/home_search.html' , {'property_list':property_list})

def place_filter(request , place):
    place = Place.objects.get(name = place)
    property_list = Property.objects.filter(place=place)
    return render(request , 'settings/home_search.html' , {'property_list':property_list})

    
def contact(request):
    site_info = Info.objects.last()

    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']


        send_mail_task.delay(subject , name,email,message)


    return render(request,'settings/contact.html',{'site_info': site_info})


def news_letters_subscribe(request):
    email = request.POST.get('emailinput')
    NewsLitter.objects.create(email=email)
    return JsonResponse({'done':'done'})