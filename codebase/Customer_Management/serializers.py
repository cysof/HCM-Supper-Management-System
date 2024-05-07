from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the customers model
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email', 'dob', 'address')


    def create(self, validated_data):
        """
        Create and return a new instance of the CustomUser model
        """
        return CustomUser.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update the existing instance of the CustomUser model
        """
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
