from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField()
    products = models.ManyToManyField(Product, related_name='service', blank=True)
