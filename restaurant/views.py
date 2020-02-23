from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Restaurant, Menu, Category, Dish, Allergen, Lifestyle
from .serializers import RestaurantSerializer, MenuSerializer, CategorySerializer, DishSerializer, AllergenSerializer, \
    LifestyleSerializer


class RestaurantViewSet(ModelViewSet):
    """
    A viewset that list restaurant instances.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class AllergenViewSet(ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer


class LifestyleViewSet(ModelViewSet):
    queryset = Lifestyle.objects.all()
    serializer_class = LifestyleSerializer
