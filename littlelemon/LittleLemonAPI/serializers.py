from django.contrib.auth.models import User
from rest_framework import serializers

import bleach;

from .models import Category, MenuItem, Booking

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'groups']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model  = Category
    fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
  class Meta:
    model  = MenuItem
    fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
  def validate_name(self, value):
    return bleach.clean(value)

  class Meta:
    model  = Booking
    fields = '__all__'