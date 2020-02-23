from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuViewSet, CategoryViewSet, DishViewSet, AllergenViewSet, LifestyleViewSet
from django.conf.urls import url, include

router = DefaultRouter()

router.register(r'restaurant', RestaurantViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'dish', DishViewSet)
router.register(r'allergen', AllergenViewSet)
router.register(r'lifestyle', LifestyleViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
