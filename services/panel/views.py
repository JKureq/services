from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import ProductForm, IngredientForm
from django.views.generic import ListView
from .models import Ingredient, Product, Service
from django.views.generic.edit import FormView, CreateView, DeleteView
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

class ProductsView(ListView):
    template_name = 'panel/products.html'
    model = Product


class ServicesView(ListView):
    template_name = 'panel/services.html'
    model = Service
