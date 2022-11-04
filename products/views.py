from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Create your views here.
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from business.models import BusinessBranch
from .forms import ProductsForm, ReviewForm
from .models import Product


def products_view(request, category_slug=None):
    products = Product.objects.all()
    businesses = BusinessBranch.objects.filter(is_approved=True)
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)

    context = {
        'products': products,
        'businesses': businesses,
    }
    return render(request, 'farm/products/index.html', context)
    # return render(request, 'shop/products/list.html', {'products': products})


def search(request):
    products = Product.objects.all()
    businesses = BusinessBranch.objects.filter(is_approved=True)
    if request.method == 'POST':
        product = request.POST.get('productSearch')
        business = request.POST.get('businessSearch')
        if product:
            products = products.filter(name__contains=product)
        if business:
            businesses = businesses.filter(name__contains=business)
            products = products.filter(branch__business__in=businesses)

    context = {
        'products': products,
        'businesses': businesses,
    }
    return render(request, 'farm/products/index.html', context)

@login_required
def add_product(request, business_slug, branch_slug):
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business__owner=request.user,
                               business__slug=business_slug)
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.branch = branch
            new_product.save()
            new_product.slug = f"{slugify(new_product.name)}-{new_product.id}"
            new_product.save()
            return redirect(branch.business.get_absolute_url())

    return render(request, 'farm/products/add_products.html', {'branch': branch, 'form': form})


@login_required
def update_product(request, business_slug, branch_slug):
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business__owner=request.user,
                               business__slug=business_slug)
    form = ProductsForm()
    return render(request, 'farm/products/add_products.html', {'branch': branch, 'form': form})


@login_required
def delete_product(request, business_slug, branch_slug):
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business__owner=request.user,
                               business__slug=business_slug)
    # branch.delete()
    # return redirect()


@login_required
@require_POST
def add_review(request, id):
    product = get_object_or_404(Product, id=id)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        new_review = review_form.save(commit=False)
        new_review.user = request.user
        new_review.product = product
        new_review.save()
        messages.success(request, "Review posted successfully")
    else:
        messages.error(request, "Invalid review data")
    return redirect(product.get_absolute_url())



