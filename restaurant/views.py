# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from .models import MenuItem
# from .serializers import MenuItemSerializer
# from .serializers import UserSerializer


# @api_view(['GET', 'POST'])
# def menu_items_view(request):
#     if request.method == 'GET':
#         menu_items = MenuItem.objects.all()
#         serializer = MenuItemSerializer(menu_items, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MenuItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def single_menu_item_view(request, pk):
#     try:
#         menu_item = MenuItem.objects.get(pk=pk)
#     except MenuItem.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MenuItemSerializer(menu_item)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MenuItemSerializer(menu_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         menu_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html', {})

# from django.contrib.auth.models import User
# from rest_framework import viewsets, permissions
# from rest_framework.response import Response

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing users.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer  # Make sure you have this serializer defined

#     # You can customize this as needed
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

# def restaurant_home(request):
#     # Your view logic here
#     return render(request, 'index.html', {})

# from rest_framework import viewsets
# from .models import Booking
# from .serializers import BookingSerializer

# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#     permission_classes = [permissions.IsAuthenticated]

# from rest_framework import generics
# from .models import Menu
# from .serializers import MenuSerializer

# class MenuItemView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking

from .serializers import MenuSerializer, BookingSerializer, UserSerializer

from django.contrib.auth.models import User


# Create your views here.

# def sayHello(request):
#  return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

# class MenuItemView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]
   
# class MenuItemsView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
   
# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#     permission_classes = [permissions.IsAuthenticated]

# from .serializers import MenuSerializer

# @api_view(['GET', 'PUT', 'DELETE'])
# def single_menu_item_view(request, pk):
#     try:
#         menu_item = MenuItem.objects.get(pk=pk)
#     except MenuItem.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MenuItemSerializer(menu_item)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MenuItemSerializer(menu_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         menu_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
   
from django.shortcuts import render
from django.core import serializers
from .models import Booking, Menu
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
