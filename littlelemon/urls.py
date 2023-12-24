"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# littlelemon/urls.py
# littlelemon/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from restaurant import views
from restaurant.views import BookingViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('restaurant/', include('restaurant.urls')),  # Include restaurant URLs under 'restaurant/'
]

# Set up the router for Django REST Framework views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Extend the urlpatterns list with the URLs from the router
urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]

#Booking 
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

# Create a router and register the BookingViewSet with it
router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='tables')

urlpatterns = [
    # Other URL patterns...
    path('api/', include(router.urls)),
    path('restaurant/booking/', include(router.urls)),
    # Other URL patterns...
]

