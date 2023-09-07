from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r'users',      views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)

app_name = "littlelemon-api"
bookings_lc = {
  'get':    'list',
  'post':   'create'
}
booking = {
  'get':    'retrieve',
}
urlpatterns = [
  path('',                                include(router.urls)),
  path('menu-items',                      views.MenuItemsView.as_view(),             name='menu-items'),
  path('menu-items/<int:pk>',             views.SingleMenuItemView.as_view(),        name='menu-item' ),
  path('bookings',                        views.BookingViewSet.as_view(bookings_lc), name='bookings'  ),
  path('bookings/<str:reservation_date>', views.BookingViewSet.as_view(booking),     name='booking'   ),
  path('api-token-auth',                  obtain_auth_token                                           ),
]