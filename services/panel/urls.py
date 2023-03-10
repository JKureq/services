from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('panel/', views.panel, name='panel'),
    path('panel/ingredients', views.IngredientsView.as_view(), name='ingredients'),
    path('panel/ingredients/add',
         views.IngredientsAddView.as_view(), name='ingredients_add'),
    path('panel/ingredients/delete/<int:pk>/',
         views.IngredientsDeleteView.as_view(), name='ingredients_delete'),
    path('panel/ingredients/update/<int:pk>/',
         views.IngredientsUpdateView.as_view(), name='ingredients_update'),
    path('panel/products', views.ProductsView.as_view(), name='products'),
    path('panel/products/add', views.ProductsAddView.as_view(), name='products_add'),
    path('panel/products/delete/<int:pk>/',
         views.ProductsDeleteView.as_view(), name='products_delete'),
    path('panel/products/update/<int:pk>/',
         views.ProductsUpdateView.as_view(), name='products_update'),
    path('panel/services', views.ServicesView.as_view(), name='services'),
    path('panel/services/add', views.ServicesAddView.as_view(), name='services_add'),
    path('panel/services/delete/<int:pk>/',
         views.ServicesDeleteView.as_view(), name='services_delete'),
    path('panel/services/update/<int:pk>/',
         views.ServicesUpdateView.as_view(), name='services_update'),
]
