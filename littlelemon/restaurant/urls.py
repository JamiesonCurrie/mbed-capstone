from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "restaurant"
urlpatterns = [
  path('',                    views.home,              name='home'),
  path('about/',              views.about,             name='about'),
  path('book/',               views.book,              name="book"),
  path('menu/',               views.menu,              name="menu"),
  path('menu_item/<int:pk>/', views.display_menu_item, name="menu-item"),
  path('tables/',             views.bookings,          name="tables"),
  path('api-token-auth/',     obtain_auth_token),
]