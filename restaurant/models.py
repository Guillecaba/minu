"""
Contains database models for the Restaurant app
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from location_field.models.plain import PlainLocationField
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()


class Restaurant(models.Model):
    """
    Store a single Restaurant entry, related to :model `auth.User`
    """
    name = models.CharField(max_length=200, verbose_name=_('name'))
    slug = models.SlugField(max_length=250, unique=True, verbose_name=_('slug'))
    address = models.CharField(max_length=100, blank=True, default='', verbose_name=_('address'))
    location = PlainLocationField(based_fields=['location'],
                                  default='-22.2876834,-49.1607606', )
    logo = models.ImageField(upload_to='map/restaurant/logo', null=True, blank=True, verbose_name=_('logo'))
    phone_number = models.CharField(max_length=25, default='', blank=True, verbose_name=_('phone number'))
    staff = models.ManyToManyField(User, related_name='restaurants', verbose_name=_('staff'))
    instagram_url = models.URLField(max_length=150, default='', blank=True, verbose_name=_('instagram URL'))
    facebook_url = models.URLField(max_length=150, default='', blank=True, verbose_name=_('facebook URL'))
    website = models.URLField(max_length=150, default='', blank=True, verbose_name=_('website'))
    twitter_url = models.URLField(max_length=150, default='', blank=True, verbose_name=_('twitter URL'))
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))
    email = models.EmailField(default='', blank=True, verbose_name=_('email'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('create at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    class Meta:
        verbose_name = _('restaurant')
        verbose_name_plural = _('restaurants')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)


class Menu(models.Model):
    """
    Store a single Menu entry, related to :model `restaurant.Restaurant` & `restaurant.Category`
    """
    title = models.CharField(max_length=200, verbose_name=_('title'))
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name=_('restaurant'))
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))
    filters_active = models.BooleanField(default=False, verbose_name=_('filters active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('create at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menus')

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    Store a single Category entry, related to :model `restaurant.Menu` & `restaurant.Dish
    """
    title = models.CharField(max_length=200, verbose_name=_('title'))
    menu = models.ManyToManyField(Menu, related_name='categories', verbose_name=_('menu'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title


class Lifestyle(models.Model):
    """
    Store a single entry of a type of lifestyle related to :model `restaurant.Dish`
    """
    title = models.CharField(max_length=200, verbose_name=_('title'))
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name=_('restaurant'))

    class Meta:
        verbose_name = _('lifestyle')
        verbose_name_plural = _('lifestyles')

    def __str__(self):
        return self.title


class Allergen(models.Model):
    """
    Store a single entry of a type of allergen related to :model `restaurant.Dish`
    """
    title = models.CharField(max_length=200, verbose_name=_('title'))
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name=_('restaurant'))

    class Meta:
        verbose_name = _('allergen')
        verbose_name_plural = _('allergens')


class Dish(models.Model):
    """
    Store a single entry , related to :model ` restaurant.Dish` 6  `restaurant.Category`
    """
    title = models.CharField(max_length=200, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(upload_to='map/dishes/image', blank=True, null=True, verbose_name=_('image'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))
    lifestyle = models.ManyToManyField(Lifestyle, related_name='dishes', verbose_name=_('lifestyle'))
    allergen = models.ManyToManyField(Allergen, related_name='dishes', verbose_name=_('allergen'))

    class Meta:
        verbose_name = _('dish')
        verbose_name_plural = _('dishes')

    def __str__(self):
        return self.title
