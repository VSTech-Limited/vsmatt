from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from geopy.geocoders import Nominatim, GoogleV3
from .forms import BusinessRegistrationForm
from .models import BusinessProfile, BusinessBranch, Category
from django.http import JsonResponse


# Create your views here.


def business(request, slug=None):
    return render(request, 'shop/business.html')


def get_business(request):
    business = BusinessBranch.objects.all().values()
    # for bs in business:
    #     print(bs)
    # category = get_object_or_404(Category, slug=slug)
    business = list(business)
    # print(business)
    return JsonResponse({'business': business})

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
