from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users',      views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
#router.register(r'tables',     views.BookingViewSet)

urlpatterns = [
  path('',                    include(router.urls)),
  path('menu-items',          views.MenuItemsView.as_view()),
  path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]