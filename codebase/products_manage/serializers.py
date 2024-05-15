from rest_framework import serializers
from .models import Product, Category, CartItem, Price



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category','stock_quantity']


class PriceSerializer(serializers.ModelSerializer):
    class Mets:
        model = Price
        fields = ['Price','created_at', 'product']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','name','price', 'quantity']
    