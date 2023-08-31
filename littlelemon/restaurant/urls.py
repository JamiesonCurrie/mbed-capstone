from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
  path('',                        views.index, name='index'),
  #path('api-auth/',               include('rest_framework.urls', namespace='rest_framework')),
  path('api-token-auth/',         obtain_auth_token),
  path('api/',                    include(router.urls)),
  path('api/menu-items',          views.MenuItemsView.as_view()),
  path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]