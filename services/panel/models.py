from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.IntegerField(null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='products', blank=True)

class Service(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='services')
