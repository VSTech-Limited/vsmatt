from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils.text import slugify

from business.models import BusinessBranch
from .forms import ProductsForm
from .models import Product


def products_view(request, category_slug=None):
    products = Product.objects.all()
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    return render(request, 'farm/products/index.html', {'products': products})
    # return render(request, 'shop/products/list.html', {'products': products})


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
