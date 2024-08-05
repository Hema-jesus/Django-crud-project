from django.contrib import admin
from newapp.models import Shop
class ShopAdmin (admin.ModelAdmin):
	list_display=['Number','Color','Size','Quantity','Price']
admin.site.register(Shop,ShopAdmin)
