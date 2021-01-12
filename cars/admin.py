from cars.models import Car
from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src= "{}" width="40" style="border-radius: 5px;"/>'.format(object.car_photo.url))
    
    thumbnail.short_description='photo'
    list_display =('id','car_title','thumbnail','color','model','year','body_style','fuel_type','is_featured','city',)
    list_display_links = ('id','thumbnail','car_title')
    list_editable = ('is_featured',)
    search_fields = ('car_title','year','model')
    list_filter = ('car_title','model',)
admin.site.register(Car, CarAdmin)