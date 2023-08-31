from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
  path('',                        views.index, name='index'),
  path('api/',                    include(router.urls)),
  path('api/menu-items',          views.MenuItemsView.as_view()),
  path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
  path('api-auth/',               include('rest_framework.urls', namespace='rest_framework')),
]