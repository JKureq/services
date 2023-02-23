from django import forms
from .models import Product, Ingredient, Service, Category, Item


class CartForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }