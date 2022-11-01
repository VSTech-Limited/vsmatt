from django.shortcuts import render

# Create your views here.
from .models import Product


def products_view(request, category_slug=None):
    products = Product.objects.all()
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    return render(request, 'shop/products/index.html', {'products': products})
    # return render(request, 'shop/products/list.html', {'products': products})
