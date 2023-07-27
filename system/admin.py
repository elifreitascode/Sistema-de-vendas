from django.contrib import admin
from .models import Produtos,Vendas
# Register your models here.
@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    ...

@admin.register(Vendas)
class VendasAdmin(admin.ModelAdmin):
    ...