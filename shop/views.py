from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import BusinessProfile, BusinessBranch


# Create your views here.


def business(request):
    bus = BusinessBranch.objects.all()
    return render(request, 'shop/business.html', {'bus': bus})
