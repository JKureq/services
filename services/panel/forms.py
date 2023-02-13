from django import forms
from .models import Product, Ingredient

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'duration']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']