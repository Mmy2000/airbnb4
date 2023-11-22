from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.
class Settings(models.Model):
    site_name = models.CharField( max_length=50)
    logo = models.ImageField( upload_to='setting/')
    phone = models.CharField( max_length=30)
    email = models.EmailField( max_length=254)
    description = models.TextField(max_length=1000)
    fb_link = models.URLField( max_length=200)
    twitter_link = models.URLField( max_length=200)
    instagram_link = models.URLField( max_length=200)
    address = models.CharField( max_length=50)

    def __str__(self):
        return self.site_name
    
class Info(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="company/")
    description = models.TextField(max_length=500)
    fb_url = models.URLField(max_length=200 , blank=True, null=True)
    twitter_url = models.URLField(max_length=200 , blank=True, null=True)
    Instgram_url = models.URLField(max_length=200 , blank=True, null=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    mail = models.EmailField( max_length=254)

    

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Info")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Info_detail", kwargs={"pk": self.pk})
    
class NewsLitter(models.Model):
    email = models.EmailField( max_length=254)
    created_at = models.DateTimeField(default=timezone.now)
    

    class Meta:
        verbose_name = ("NewsLitter")
        verbose_name_plural = ("NewsLitter")

    def __str__(self):
        return self.email



    