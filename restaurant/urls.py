from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet
from django.conf.urls import url, include

router = DefaultRouter()

router.register(r'restaurant', RestaurantViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
