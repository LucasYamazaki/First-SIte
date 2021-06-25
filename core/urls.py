from core.models import Product
from django.urls import path

from .views import index, contato, product


urlpatterns = [
    path('', index, name = 'index'),
    path('contato', contato, name = 'contato'),
    path('product/<int:pk>', product, name='product'),
]