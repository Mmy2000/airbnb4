from django.contrib import admin
from . models import Property , PropertyBook , Place , PropertyImages , PropertyReview , Category
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name' , 'price','category'  ,'check_avilability']

admin.site.register(Property,SomeModelAdmin)

class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property' , 'in_progress' ]

admin.site.register(PropertyReview)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(PropertyBook,PropertyBookAdmin)
admin.site.register(Category)
# Register your models her
# Register your models here.
