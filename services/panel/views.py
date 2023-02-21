from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import ProductForm, IngredientForm, ServiceForm, CategoryForm, CartForm
from django.views.generic import ListView
from .models import Ingredient, Product, Service, Category, Item
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
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

class CartView(ListView):
    template_name = 'panel/cart.html'
    model = Item
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartForm()
        return context
    

class CartAddView(CreateView):
    template_name = 'panel/cart.html'
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('cart')


class CategoriesView(ListView):
    template_name = 'panel/categories.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context


class CategoriesAddView(CreateView):
    template_name = 'panel/categories.html'
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('categories')


class IngredientsView(ListView):
    template_name = 'panel/ingredients.html'
    model = Ingredient
    context_object_name = 'ingredients'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IngredientForm()
        context['cat'] = str(self.kwargs['category'])
        return context
    
class IngredientsAddView(CreateView):
    template_name = 'panel/ingredients.html'
    model = Ingredient
    form_class = IngredientForm
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
    paginate_by = 10

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
    paginate_by = 10

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


