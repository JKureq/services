from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import ProductForm, IngredientForm, ServiceForm
from django.views.generic import ListView
from .models import Ingredient, Product, Service
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
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
    template_name = 'panel/ingredients.html'
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients')

class IngredientsDeleteView(DeleteView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients')
    template_name = 'panel/ingredients_delete.html'


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
    template_name = 'panel/products.html'
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
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ServiceForm()
        return context

class ServicesAddView(CreateView):
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('services')
    


class ServicesDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('services')


class ServicesUpdateView(UpdateView):
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('services')
    template_name = 'panel/services_update.html'
