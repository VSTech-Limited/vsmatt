from django.shortcuts import render

from .models import BusinessProfile, BusinessBranch


# Create your views here.


def business(request):
    bus = BusinessBranch.objects.all()
    return render(request, 'shop/business.html', {'bus': bus})
