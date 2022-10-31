from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from geopy.geocoders import Nominatim, GoogleV3
from .forms import BusinessRegistrationForm
from .models import BusinessProfile, BusinessBranch, ProductCategory, Product
from django.http import JsonResponse


# Create your views here.


def products_view(request, category_slug=None):
    products = Product.objects.all()
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    return render(request, 'shop/products/list.html', {'products': products})


def businesses(request, slug=None):
    return render(request, 'shop/business.html')


@login_required
def register_business(request):
    bs_reg_form = BusinessRegistrationForm()
    if request.method == 'POST':
        form = BusinessRegistrationForm(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            cd = form.cleaned_data
            new_bs = form.save(commit=False)
            new_bs.name = slugify(cd['name'])
            new_bs.owner = request.user
            geolocator = GoogleV3(settings.GOOGLE_MAPS_API_KEY)
            location = geolocator.reverse((Decimal(cd['latitude']), Decimal(cd['longitude'])))

            # try:
            #     print(location)
            new_bs.address = location
            # except AttributeError:
            #     messages.error(request, "The address is invalid")
            new_bs.save()
            return redirect('home')

    return render(request, "shop/register_business.html", {'bs_reg_form': bs_reg_form})


@login_required
def register_branch(request, bs_id):
    business_profile = get_object_or_404(BusinessProfile, id=bs_id, owner=request.user)
    branch_reg_form = BusinessRegistrationForm()
    if request.method == 'POST':
        form = BusinessRegistrationForm(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            cd = form.cleaned_data
            new_branch = form.save(commit=False)
            new_branch.name = slugify(cd['name'])
            new_branch.business = business_profile
            geolocator = GoogleV3(settings.GOOGLE_MAPS_API_KEY)
            location = geolocator.reverse((Decimal(cd['latitude']), Decimal(cd['longitude'])))
            # try:
            #     print(location)
            new_branch.address = location
            # except AttributeError:
            #     messages.error(request, "The address is invalid")
            new_branch.save()
            return redirect('home')
    return render(request, "shop/register_business.html", {'bs_reg_form': branch_reg_form})


@login_required
def add_product(request, bs_slug, br_slug):
    branch = get_object_or_404(BusinessBranch, slug=br_slug, business__owner=request.user, business__slug=bs_slug)
    return render(request, 'shop/add_products.html', {'branch': branch})


@login_required
def business_list(request):
    businesses = BusinessProfile.objects.filter(owner=request.user)
    return render(request, "shop/my_business.html", {'businesses': businesses})


@login_required
def business_detailed(request, bs_id, bs_slug):
    business = get_object_or_404(BusinessProfile, id=bs_id, slug=bs_slug)
    return render(request, "shop/business_detailed.html", {'business': business})


def view_business_products(request, business_slug, branch_slug):
    return render(request, "shop/business/index.html")
