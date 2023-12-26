# from django.urls import path
# from .views import menu_items_view, single_menu_item_view

# urlpatterns = [
#     path('menu/items/', menu_items_view, name='menu-list-create'),
#     path('menu/items/<int:pk>/', single_menu_item_view, name='menu-detail'),
# ]
# restaurant/views.py
# restaurant/views.py
# from django.shortcuts import render

# def restaurant_home(request):
#     # Your view logic here
#     return render(request, 'restaurant_home.html', {})

# # restaurant/urls.py
# from django.urls import path
# from . import views
# from .views import restaurant_home, menu_items_view, single_menu_item_view

# urlpatterns = [
#     path('', restaurant_home, name='restaurant-home'),
#     path('menu/items/', menu_items_view, name='menu-list-create'),
#     path('menu/items/<int:pk>/', single_menu_item_view, name='menu-detail'),
#     path('menu/', views.MenuItemView.as_view(), name='menu-list-create'),
#     path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
# ]

# from django.contrib import admin 
# from rest_framework import routers
# from django.urls import path 
# from . import views
# from rest_framework.authtoken.views import obtain_auth_token
  
# urlpatterns = [ 
#     path('', views.index, name='index'), 
#     path('menu/', views.MenuItemView.as_view()),
#     path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
#     path('menu-items/', views.MenuItemView.as_view()),
#     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
#     path('message/', views.msg),
#     path('api-token-auth/', obtain_auth_token)
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

urlpatterns = [
path('api-token-auth/', obtain_auth_token),
path('menu/', views.MenuItemView.as_view()),
path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
path('',TemplateView.as_view(template_name='index.html'), name='indexpage'),
]