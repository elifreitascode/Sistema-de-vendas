from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_login),
    path('signup/', views.home_signup)
]