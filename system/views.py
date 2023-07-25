from django.shortcuts import render
from .models import Produtos

def home(request):
    return render(request, 'system/pages/paginainicial.html')
# Create your views here.
def vendas(request, id):
    return render(request, 'system/pages/vendas.html')
def produtos(request,id):
    produtos = Produtos.objects.all()
    tem_produtos = len(produtos)
    if tem_produtos > 0:
        return render(request, 'system/pages/produtos.html', context={
            'tem_produtos': tem_produtos,
            'produtos': produtos, 
        })
def clientes(request, id):
    return render(request, 'system/pages/clientes.html')