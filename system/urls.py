from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('vendas/<int:id>/', views.vendas),
    path('produtos/<int:id>/', views.produtos),
    path('clientes/<int:id>/', views.clientes),
]