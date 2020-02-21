from rest_framework.serializers import ModelSerializer
from .models import Restaurant


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', ]

    def save(self, *kwargs):
        restaurant = super().save()
        restaurant.staff.add(self.context['request'].user)
        return restaurant
