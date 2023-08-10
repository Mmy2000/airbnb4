from django.contrib import admin
from . models import Property , PropertyBook , Place , PropertyImages , PropertyReview , Category
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(PropertyReview)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Property,SomeModelAdmin)
admin.site.register(PropertyBook)
admin.site.register(Category)
# Register your models her
# Register your models here.
