from django.shortcuts import render


def home(request):
    return render(request, 'system/paginainicial.html')
# Create your views here.
