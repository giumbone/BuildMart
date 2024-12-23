from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

def product_list(request):
    if 'products_list' in cache:
        products = cache.get('products_list')
    else:
        products = Product.objects.all()
        cache.set('products_list', products, 300)
    return render(request, 'yourapp/product_list.html', {'products': products})

def product_detail(request, id):
    cache_key = f'product_{id}'
    if cache_key in cache:
        product = cache.get(cache_key)
    else:
        product = get_object_or_404(Product, pk=id)
        cache.set(cache_key, product, 300)
    return render(request, 'yourapp/product_detail.html', {'product': product})

def clear_product_cache(request, id=None):
    if id:
        cache_key = f'product_{id}'
        cache.delete(cache_key)
        return HttpResponse(f"Cache cleared for product {id}")
    else:
        cache.delete('products_list')
        return HttpResponse("Cache cleared for all products")

from django.urls import path
from .views import clear_product_cache

urlpatterns = [
    path('clear-cache/', clear_product_cache, name='clear_cache'),
    path('clear-cache/<int:id>/', clear_product_cache, name='clear_product_cache'),
]