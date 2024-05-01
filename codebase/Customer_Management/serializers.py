from rest_framework import serializers
from .models import CustomerBio, Purches


class CustomerBioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBio
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'dob', 'address']

class PurcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purches
        fields = ['id', 'customer', 'products', 'price']
