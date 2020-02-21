from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    """
    A viewset that list restaurant instances.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
