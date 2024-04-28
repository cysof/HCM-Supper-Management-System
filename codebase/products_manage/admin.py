from django.contrib import admin
from .models import Product, Price

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock']
    list_filter = ['price']

class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)