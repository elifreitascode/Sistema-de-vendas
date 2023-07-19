from django.shortcuts import render


def home(request):
    return render(request, 'system/pages/paginainicial.html')
# Create your views here.
def vendas(request, id):
    return render(request, 'system/pages/vendas.html')
def produtos(request,id):
    return render(request, 'system/pages/produtos.html')
def clientes(request, id):
    return render(request, 'system/pages/clientes.html')