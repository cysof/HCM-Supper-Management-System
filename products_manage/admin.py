from django.contrib import admin
from .models import Product,CartItem,Category,Order,OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock_quantity']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','status', 'created_at']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product','quantity']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Product, ProductAdmin)