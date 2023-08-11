from django.shortcuts import render
from django.http import HttpResponse

def home_login(request):
    return render(request,'login/pages/login.html')
def home_signup(request):
    return render(request, 'login/pages/signup.html')

