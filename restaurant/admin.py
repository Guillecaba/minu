from django.contrib import admin
from .models import Restaurant, Menu, Category, Dish, Lifestyle, Allergen

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Lifestyle)
admin.site.register(Allergen)
