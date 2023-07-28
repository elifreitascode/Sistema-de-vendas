from django.shortcuts import render
from .models import Produtos, Vendas

def home(request):
    return render(request, 'system/pages/paginainicial.html')

# Create your views here.
def vendas(request, id):
    venda = Vendas.objects.all()
    tem_vendas = len(venda)
    if tem_vendas > 0:
        return render(request, 'system/pages/vendas.html', context={
            'tem_vendas': tem_vendas,
            'venda': venda,
        })
    else:
        return render(request, 'system/pages/vendas.html',
        )


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