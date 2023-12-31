from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify 
from django.db.models import Avg , Count



# Create your models here.
class Property(models.Model):
    owner = models.ForeignKey(User, related_name='property_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place',related_name='property_place',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',related_name='property_category',on_delete=models.CASCADE)
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField(null=True,blank=True)
    views = models.PositiveIntegerField(default=0)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Property,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("property:property_detail", kwargs={"slug": self.slug})
    
    def avr_review(self):
        reviews = PropertyReview.objects.filter(property=self , status=True).aggregate(average=Avg('rating'))
        avg =0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def count_review(self):
        reviews = PropertyReview.objects.filter(property=self , status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
        
    def check_avilability(self):
        all_reservations = self.book_property.all()
        now = timezone.now().date()
        for reservation in all_reservations:
            if now > reservation.date_to :
                return 'available'
            elif now > reservation.date_from and now < reservation.date_to:
                reserved_to = reservation.date_to
                return f'in progress{reserved_to}'
        else :
            return 'available'
        
    
    

class PropertyImages(models.Model):
    property = models.ForeignKey(Property,related_name='property_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyimages/')

    def __str__(self):
        return str(self.property)

class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60)
    icons = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class PropertyReview(models.Model):
    user = models.ForeignKey(User, related_name="review_auther", on_delete=models.CASCADE)
    property = models.ForeignKey("Property", related_name="review_property", on_delete=models.CASCADE)
    rating = models.FloatField()
    subject = models.CharField( max_length=50,blank=True)
    review = models.TextField(max_length=2000,blank=True)
    ip = models.CharField( max_length=50,blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return str(self.property)
    

count = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)
    
class PropertyBook(models.Model):
    user = models.ForeignKey(User, related_name="book_owner", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name="book_property", on_delete=models.CASCADE)
    date_from = models.DateField( default=timezone.now)
    date_to = models.DateField( default=timezone.now)
    guest = models.IntegerField( choices=count)
    children = models.IntegerField( choices=count)

    def __str__(self):
        return str(self.property)
    
    def in_progress(self):
        now = timezone.now().date()
        return now > self.date_from and now < self.date_to
    in_progress.boolean = True