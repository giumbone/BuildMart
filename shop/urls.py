from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    # Check if the product list is in cache
    if 'products_list' in cache:
        products = cache.get('products_list')
    else:
        products = Product.objects.all()
        # Cache the product list for 300 seconds (5 minutes)
        cache.set('products_list', products, 300)
    return render(request, 'yourapp/product_list.html', {'products': products})

def product_detail(request, id):
    cache_key = f'product_{id}'
    # Check if the product details are in cache
    if cache_key in cache:
        product = cache.get(cache_key)
    else:
        product = get_object_or_404(Product, pk=id)
        # Cache the product detail for 300 seconds (5 minutes)
        cache.set(cache_key, product, 300)
    return render(request, 'yourapp/product_detail.html', {'product': product})