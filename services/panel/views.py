from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import ProductForm, IngredientForm
from django.views.generic import ListView
from .models import Ingredient, Product, Service
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    if request.method == 'POST':
        logout(request)

    return render(request, 'panel/index.html')
    

def panel(request):
    form = ProductForm()
    return render(request, 'panel/panel.html', {
        'form': form,
    })

class IngredientsView(ListView):
    template_name = 'panel/ingredients.html'
    model = Ingredient
    context_object_name = 'ingredients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IngredientForm()
        return context
    
    

class IngredientsAddView(CreateView):
    model = Ingredient
    fields = ['name']
    success_url = reverse_lazy('ingredients')


class IngredientsDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('ingredients')


class IngredientsUpdateView(UpdateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients')
    template_name = 'panel/ingredients_update.html'
    

class ProductsView(ListView):
    template_name = 'panel/products.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        return context


class ProductsAddView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


class ProductsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products')


class ProductsUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')
    template_name = 'panel/products_update.html'


class ServicesView(ListView):
    template_name = 'panel/services.html'
    model = Service
