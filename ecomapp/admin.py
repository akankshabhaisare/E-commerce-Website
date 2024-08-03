from django.contrib import admin
from ecomapp.models import Product

# Register your models here.
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','is_active','pdetail','cat']
    list_filter=['cat','is_active']


admin.site.register(Product,ProductAdmin)