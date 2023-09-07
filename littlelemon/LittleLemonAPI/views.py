from django.contrib.auth.models import User

from rest_framework import viewsets, generics, mixins, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from .models      import Category, MenuItem, Booking
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
  permission_classes = [IsAuthenticatedOrReadOnly]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset         = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
  queryset           = Booking.objects.all()
  serializer_class   = BookingSerializer
  permission_classes = [AllowAny]

  def retrieve(self, request, reservation_date=None):
    split_date = reservation_date.split('-')
    bookings   = self.get_queryset().filter(reservation_date__year=split_date[0], reservation_date__month=split_date[1], reservation_date__day=split_date[2])
    if not bookings.exists():
      serializer = self.get_serializer(self.get_queryset().none(), many=True)
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    serializer = self.get_serializer(bookings, many=True)

    return Response(serializer.data)