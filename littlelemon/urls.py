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
# # littlelemon/urls.py
# # littlelemon/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from rest_framework.routers import DefaultRouter
# from restaurant import views
# #from restaurant.views import BookingViewSet


# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('auth/', include('djoser.urls')),
# #     path('auth/', include('djoser.urls.authtoken')),
# #     path('', views.index, name='index'),
# #     path('restaurant/menu/', include('restaurant.urls')),  # Include restaurant URLs under 'restaurant/'
# # ]

# # Set up the router for Django REST Framework views
# # router = routers.DefaultRouter()
# # #router.register(r'users', views.UserViewSet)
# # router.register(r'tables', views.BookingViewSet)

# # Extend the urlpatterns list with the URLs from the router
# # urlpatterns += [
# #     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# #     path('', include(router.urls)),
# # ]

# # #Booking 
# # from rest_framework.routers import DefaultRouter
# # from restaurant.views import BookingViewSet

# # # Create a router and register the BookingViewSet with it
# # router = DefaultRouter()
# # router.register(r'tables', BookingViewSet, basename='tables')

# urlpatterns = [
#     # Other URL patterns...
#     path('admin/', admin.site.urls),
#     path('restaurant/', include('restaurant.urls')),
#     path('restaurant/menu/', include('restaurant.urls')),
#     path('restaurant/booking/', include(router.urls)),
#     path('api/',include('LittleLemonAPI.urls')),
#     path('auth/', include('djoser.urls')),
#     path('auth/', include('djoser.urls.authtoken')),

#     #path('api/', include(router.urls)),
#     #path('restaurant/menu/', include(router.urls)),
#     #path('restaurant/booking/', include(router.urls)),
#         # Other URL patterns...
# ]

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework import routers

# from restaurant import views

# from restaurant.views import BookingViewSet

# router = routers.DefaultRouter()
# router.register(r'tables', BookingViewSet, basename='tables')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('restaurant/', include('restaurant.urls')),
#     path('restaurant/menu/', include('restaurant.urls')),
#     path('restaurant/booking/', include(router.urls)),
#     path('api/',include('LittleLemonAPI.urls')),
#     path('auth/', include('djoser.urls')),
#     path('auth/', include('djoser.urls.authtoken')),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet
from restaurant import views
router = DefaultRouter()

router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('restaurant.urls')),
    path('restaurant/',include('restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('restaurant/booking/', include(router.urls)),
    ]