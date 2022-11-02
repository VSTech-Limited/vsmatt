from decimal import Decimal

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from django.utils.text import slugify

from geo.geofactory import GeoMapQuestFactory
from .forms import BusinessRegistrationForm, BranchRegistrationForm
from .models import BusinessProfile, BusinessBranch


@login_required
def register_business(request):
    geo = GeoMapQuestFactory.createReverse(settings.MAPS_QUEST_API_KEY)
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
            lat = Decimal(cd['latitude'])
            lng = Decimal(cd['longitude'])
            data = geo.reverse((lat, lng))[0]
            location = data.results[0].locations[0]
            address = f"{location.street}, {location.admin_area4}"
            new_bs.address = address
            messages.error(request, "The address is invalid")
            new_bs.save()
            new_bs.slug = f"{slugify(cd['name'])}-{new_bs.id}"
            new_bs.save()
            return redirect('index')
    return render(request, "farm/register_business.html", {'bs_reg_form': bs_reg_form})


@login_required
def register_branch(request, business_slug):
    geo = GeoMapQuestFactory.createReverse(settings.MAPS_QUEST_API_KEY)
    business_profile = get_object_or_404(BusinessProfile, slug=business_slug, owner=request.user)
    branch_reg_form = BranchRegistrationForm()
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
            lat = Decimal(cd['latitude'])
            lng = Decimal(cd['longitude'])
            data = geo.reverse((lat, lng))[0]
            location = data.results[0].locations[0]
            address = f"{location.street}, {location.admin_area4}"
            new_branch.address = address
            new_branch.save()
            return redirect('home')
    return render(request, "farm/register_business.html", {'bs_reg_form': branch_reg_form})


@login_required
def own_businesses_list(request):
    businesses = BusinessProfile.objects.filter(owner=request.user)
    return render(request, "farm/own_business.html", {'businesses': businesses})


@login_required
def own_business_detailed(request, business_slug):
    business = get_object_or_404(BusinessProfile, slug=business_slug)
    return render(request, "farm/business/business_detailed.html", {'business': business})


def own_business_branch_detailed(request, business_slug, branch_slug):
    return render(request, "farm/own_business.html")


def businesses(request, category_slug=None):
    businesses = BusinessBranch.objects.all()
    if category_slug:
        businesses = BusinessProfile.objects.filter(category__slug=category_slug)
    return render(request, 'farm/business/index.html', {'businesses': businesses})
