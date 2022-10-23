from django.shortcuts import render

from .models import BusinessProfile, BusinessBranch, Category


# Create your views here.


def business(request, slug=None):
    if slug:
        pass
    categories = Category.objects.all()
    bus = BusinessBranch.objects.all()
    return render(request, 'shop/business.html', {'bus': bus,'categories': categories})
