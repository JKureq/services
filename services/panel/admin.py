from django.contrib import admin
from .models import Product, Service, Ingredient, Category

# Register your models here.




admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Ingredient)
admin.site.register(Category)

