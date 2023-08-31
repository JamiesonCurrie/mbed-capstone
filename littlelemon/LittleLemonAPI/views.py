from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Category, MenuItem, Booking
from .serializers import UserSerializer, CategorySerializer, MenuItemSerializer, BookingSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset           = User.objects.all()
  serializer_class   = UserSerializer
  permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
  queryset           = Category.objects.all()
  serializer_class   = CategorySerializer
  permission_classes = [IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
  queryset         = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset         = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
  queryset         = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]
