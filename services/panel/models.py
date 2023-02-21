from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True, blank= False)
    price = models.IntegerField(blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='items', null=False, blank=False)
    
    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='categories', null=False, blank=False)
    
    def __str__(self):
       return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='ingredients', null=True, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ingredients', null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    price = models.IntegerField(blank=False)
    duration = models.IntegerField(null=True, blank=False)
    ingredients = models.ManyToManyField(
        Ingredient, related_name='products', blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products', null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date = models.DateField(blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name='services')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='services', null=False, blank=False)
