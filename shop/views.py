from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from products.forms import ReviewForm
from cart.forms import CartAddProductForm
# Create your views here.
from business.models import BusinessBranch, BusinessProfile
from products.models import Product, ProductCategory


def index(request, business_slug, branch_slug):
    business = get_object_or_404(BusinessProfile, slug=business_slug)
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business=business)
    products = branch.products.all()
    categories = ProductCategory.objects.filter(product__in=products)
    context = {
        'business': business,
        'branch': branch,
        'categories': categories
    }
    return render(request, "farm/shop/index.html", context)


def product_detailed(request, business_slug, branch_slug, product_slug):
    form = CartAddProductForm()
    review_form = ReviewForm()
    business = get_object_or_404(BusinessProfile, slug=business_slug)
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business=business)
    product = get_object_or_404(Product, slug=product_slug)
    categories = ProductCategory.objects.filter(product__in=branch.products.all())
    context = {
        'business': business,
        'branch': branch,
        'product': product,
        'categories': categories,
        'form': form,
        'review_form': review_form
    }
    return render(request, "farm/shop/detail.html", context)


def products_list(request, business_slug, branch_slug, category_slug=None):
    business = get_object_or_404(BusinessProfile, slug=business_slug)
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business=business)
    products = branch.products.all()
    categories = ProductCategory.objects.filter(product__in=products)
    if category_slug:
        products = branch.products.filter(category__slug=category_slug)
    context = {
        'business': business,
        'branch': branch,
        'products': products,
        'categories': categories
    }
    return render(request, "farm/shop/list.html", context)



