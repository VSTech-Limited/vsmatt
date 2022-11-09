from decimal import Decimal

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from products.models import ProductCategory
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
            address = f"{location.street}" \
                      f" {location.admin_area5 if not location.admin_area4 else ''} " \
                      f"{location.admin_area4} {location.postal_code}"
            new_bs.address = address
            messages.error(request, "The address is invalid")
            new_bs.save()
            new_bs.slug = f"{slugify(cd['name'])}-{new_bs.id}"
            new_bs.save()
            return redirect('business:own_business_list')
    return render(request, "farm/register_business.html", {'bs_reg_form': bs_reg_form})


@login_required
def delete_business(request, business_slug):
    business_profile = get_object_or_404(BusinessProfile, slug=business_slug, owner=request.user)
    business_profile.delete()
    return redirect('business:own_business_list')


@login_required
def update_business(request, business_slug):
    business_profile = get_object_or_404(BusinessProfile, slug=business_slug, owner=request.user)
    geo = GeoMapQuestFactory.createReverse(settings.MAPS_QUEST_API_KEY)
    bs_reg_form = BusinessRegistrationForm(instance=business_profile)
    if request.method == 'POST':
        form = BusinessRegistrationForm(
            data=request.POST,
            files=request.FILES,
            instance=business_profile
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
            address = f"{location.street}" \
                      f" {location.admin_area5 if not location.admin_area4 else ''} " \
                      f"{location.admin_area4} {location.postal_code}"
            new_bs.address = address
            messages.error(request, "The address is invalid")
            new_bs.save()
            new_bs.slug = f"{slugify(cd['name'])}-{new_bs.id}"
            new_bs.save()
            return redirect('business:own_business_list')
        else:
            print("eRROE")
    return render(request, "farm/register_business.html", {'bs_reg_form': bs_reg_form})


@login_required
def register_branch(request, business_slug):
    geo = GeoMapQuestFactory.createReverse(settings.MAPS_QUEST_API_KEY)
    business_profile = get_object_or_404(BusinessProfile, slug=business_slug, owner=request.user)
    branch_reg_form = BranchRegistrationForm()
    if request.method == 'POST':
        branch_reg_form = BranchRegistrationForm(
            data=request.POST,
            files=request.FILES
        )
        if branch_reg_form.is_valid():
            cd = branch_reg_form.cleaned_data
            new_branch = branch_reg_form.save(commit=False)
            new_branch.business = business_profile
            lat = Decimal(cd['latitude'])
            lng = Decimal(cd['longitude'])
            data = geo.reverse((lat, lng))[0]
            location = data.results[0].locations[0]
            address = f"{location.street}" \
                      f" {location.admin_area5 if not location.admin_area4 else ''} " \
                      f"{location.admin_area4} {location.postal_code}"
            new_branch.address = address
            print(f"{new_branch.business.owner.id=}")
            new_branch.save()
            new_branch.slug = f"{slugify(cd['name'])}-{new_branch.id}"
            new_branch.save()
            return redirect(business_profile.get_absolute_url())
    return render(request, "farm/register_business.html", {'bs_reg_form': branch_reg_form})


@login_required
def delete_branch(request, business_slug, branch_slug):
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business__owner=request.user,
                               business__slug=business_slug)
    branch.delete()
    return redirect(branch.business.get_absolute_url())


@login_required
def update_branch(request, business_slug, branch_slug):
    geo = GeoMapQuestFactory.createReverse(settings.MAPS_QUEST_API_KEY)

    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business__owner=request.user,
                               business__slug=business_slug)
    branch_reg_form = BranchRegistrationForm(instance=branch)
    if request.method == 'POST':
        branch_reg_form = BranchRegistrationForm(
            instance=branch,
            data=request.POST,
            files=request.FILES
        )
        if branch_reg_form.is_valid():
            cd = branch_reg_form.cleaned_data
            new_branch = branch_reg_form.save(commit=False)
            lat = Decimal(cd['latitude'])
            lng = Decimal(cd['longitude'])
            data = geo.reverse((lat, lng))[0]
            location = data.results[0].locations[0]
            address = f"{location.street}" \
                      f" {location.admin_area5 if not location.admin_area4 else ''} " \
                      f"{location.admin_area4} {location.postal_code}"
            new_branch.address = address
            new_branch.save()
            new_branch.slug = f"{slugify(cd['name'])}-{new_branch.id}"
            new_branch.save()
            return redirect(new_branch.business.get_absolute_url())

    return render(request, "farm/register_business.html", {'bs_reg_form': branch_reg_form})


@login_required
def own_businesses_list(request):
    businesses = BusinessProfile.objects.filter(owner=request.user)
    return render(request, "farm/own_business.html", {'businesses': businesses})


@login_required
def own_business_detailed(request, business_slug):
    business = get_object_or_404(BusinessProfile, slug=business_slug, owner=request.user)
    return render(request, "farm/business_detailed.html", {'business': business})
    
@login_required
def orders(request):
    businesses = BusinessProfile.objects.filter(owner=request.user)
    branches = BusinessBranch.objects.filter(business__in=businesses)
    return render(request, "farm/orders.html", {'businesses': businesses, 'branches':branches})


def own_business_branch_detailed(request, business_slug, branch_slug):
    return render(request, "farm/own_business.html")


def businesses(request, category_slug=None):
    businesses = BusinessBranch.objects.all()
    if category_slug:
        businesses = BusinessBranch.objects.filter(category__slug=category_slug)
    return render(request, 'farm/business/index.html', {
        'businesses': businesses,
        'title': "Businesses",
        'categories': category_slug
    })


