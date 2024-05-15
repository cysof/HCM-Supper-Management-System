from rest_framework import serializers
from .models import CustomUser, Purches, Product, Price

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'dob', 'address']

class PurchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purches
        fields = ['id', 'customer', 'products', 'price']