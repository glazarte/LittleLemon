from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu
from .models import Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # Include all fields from the Menu model

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'