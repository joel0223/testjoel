from django.urls import path
from .views import bienvenue

urlpatterns = [
    path('', bienvenue, name='bienvenue'),
]
