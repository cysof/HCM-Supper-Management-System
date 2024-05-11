from django.contrib import admin
from .models import Product, Price, Category, CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock_quantity']
    list_filter = ['price']

class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']

admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem, CartItemsAdmin)