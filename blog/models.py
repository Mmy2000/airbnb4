from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify 



class Post(models.Model):
    auther = models.ForeignKey(User, related_name="post_auther", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tag = TaggableManager()
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField( default=timezone.now)
    description = models.TextField(max_length=100000)
    category = models.ForeignKey('Category',related_name='property_category',on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)



class Category(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    


