from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
  path('',                views.home,  name='home'),
  path('about/',          views.about, name='about'),
  path('api-token-auth/', obtain_auth_token),
]