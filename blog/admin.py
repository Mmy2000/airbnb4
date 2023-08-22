from django.contrib import admin
from tof.admin import TofAdmin, TranslationTabularInline
from . models import Post , Category



class CategoryAdmin(TofAdmin):
    list_display = ['id' , 'name']
    inlines = (TranslationTabularInline, )

admin.site.register(Post)
admin.site.register(Category,CategoryAdmin)
# Register your models her
# Register your models here.
