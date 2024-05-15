from rest_framework import serializers
from .models import Product, CartItem, Price


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']
    
class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['created_at', 'product', 'price']
