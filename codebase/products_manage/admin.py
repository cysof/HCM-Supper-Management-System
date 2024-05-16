from django.contrib import admin
from .models import Product,CartItem,Price,Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock_quantity']
    list_filter = ['price']

class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'price']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']



admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)