from rest_framework.serializers import ModelSerializer
from .models import Restaurant, Menu, Category, Dish, Allergen, Lifestyle


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ('created_at', 'updated_at')

    def save(self, *kwargs):
        restaurant = super().save()
        restaurant.staff.add(self.context['request'].user)
        return restaurant


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        exclude = ('created_at', 'updated_at')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at', 'updated_at')


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        exclude = ('created_at', 'updated_at')


class AllergenSerializer(ModelSerializer):
    class Meta:
        model = Allergen
        exclude = ('created_at', 'updated_at')


class LifestyleSerializer(ModelSerializer):
    class Meta:
        model = Lifestyle
        exclude = ('created_at', 'updated_at')
