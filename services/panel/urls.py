from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('panel/', views.panel, name='panel'),
    path('panel/ingredients', views.IngredientsView.as_view(), name='ingredients'),
    path('panel/ingredients/add', views.IngredientsAddView.as_view(), name='ingredients_add'),
    path('panel/ingredients/delete',views.IngredientsDeleteView.as_view(), name='ingredients_delete'),
    path('panel/products', views.ProductsView.as_view(), name='products'),
    path('panel/services', views.ServicesView.as_view(), name='services'),
]
