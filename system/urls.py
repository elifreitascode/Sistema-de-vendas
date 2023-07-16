from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('vendas/<int:id>', views.vendas)
]