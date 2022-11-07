from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from business.forms import ContactForm
from products.forms import ReviewForm
from cart.forms import CartAddProductForm
from business.forms import BranchReviewForm
# Create your views here.
from django.contrib import messages
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

def reviews(request, business_slug, branch_slug):
    form = BranchReviewForm()
    business = get_object_or_404(BusinessProfile, slug=business_slug)
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business=business)
    products = branch.products.all()
    categories = ProductCategory.objects.filter(product__in=products)
    if request.method == 'POST':
        form = BranchReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.business = branch
            new_review.save()
            messages.success(request, "Review dropped successfully!!")
    context = {
        'business': business,
        'branch': branch,
        'categories': categories,
        'form': form
    }
    return render(request, "farm/shop/reviews.html", context)


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


def contact(request, business_slug, branch_slug):
    form = ContactForm()
    business = get_object_or_404(BusinessProfile, slug=business_slug)
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business=business)
    products = branch.products.all()
    categories = ProductCategory.objects.filter(product__in=products)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.business = business
            new_contact.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect(reverse(
                'shop:shop',
                args=[
                    business_slug,
                    branch_slug
                ]
            ))
    context = {
        'form': form,
        'business': business,
        'branch': branch,
        'products': products,
        'categories': categories
    }
    return render(request, 'farm/shop/contact.html', context)
