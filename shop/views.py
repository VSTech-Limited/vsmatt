from django.shortcuts import render

from .models import BusinessProfile, BusinessBranch, Category


# Create your views here.


def business(request, slug=None):
    bus = BusinessBranch.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/business.html', {'bus': bus})
