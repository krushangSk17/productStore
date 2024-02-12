from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email')  # Include any other fields as necessary

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = Products

        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = Category

        fields = '__all__'