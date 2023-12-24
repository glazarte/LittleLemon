# from django.urls import path
# from .views import menu_items_view, single_menu_item_view

# urlpatterns = [
#     path('menu/items/', menu_items_view, name='menu-list-create'),
#     path('menu/items/<int:pk>/', single_menu_item_view, name='menu-detail'),
# ]
# restaurant/views.py
# restaurant/views.py
from django.shortcuts import render

def restaurant_home(request):
    # Your view logic here
    return render(request, 'restaurant_home.html', {})

# restaurant/urls.py
from django.urls import path
from .views import restaurant_home, menu_items_view, single_menu_item_view

urlpatterns = [
    path('', restaurant_home, name='restaurant-home'),
    path('menu/items/', menu_items_view, name='menu-list-create'),
    path('menu/items/<int:pk>/', single_menu_item_view, name='menu-detail'),
]
