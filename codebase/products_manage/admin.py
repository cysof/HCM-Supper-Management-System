from django.contrib import admin
from .models import Product,CartItem,Price

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock_quantity']
    list_filter = ['price']

class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'price']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)