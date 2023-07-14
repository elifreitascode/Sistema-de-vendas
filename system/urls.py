from django.urls import path
from system.views import home

urlpatterns = [
    path('home/', home),
]