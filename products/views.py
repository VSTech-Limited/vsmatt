from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from business.models import BusinessBranch
from .models import Product


def products_view(request, category_slug=None):
    products = Product.objects.all()
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    return render(request, 'shop/products/index.html', {'products': products})
    # return render(request, 'shop/products/list.html', {'products': products})


@login_required
def add_product(request, bs_slug, br_slug):
    branch = get_object_or_404(BusinessBranch, slug=br_slug, business__owner=request.user, business__slug=bs_slug)
    return render(request, 'shop/add_products.html', {'branch': branch})
