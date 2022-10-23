from django.shortcuts import render, get_object_or_404

from .models import BusinessProfile, BusinessBranch, Category


# Create your views here.


def business(request, slug=None):
    if slug:
        pass
    categories = Category.objects.all()
    bus = BusinessBranch.objects.all()
    return render(request, 'shop/business.html', {'bus': bus, 'categories': categories})


def add_business_location(request, slug):
    category = get_object_or_404(Category, slug=slug)
