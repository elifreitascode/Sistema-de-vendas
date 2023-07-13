from django.urls import path
from login.views import home_login

urlpatterns = [
    path('', home_login),
]