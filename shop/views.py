from django.shortcuts import render, get_object_or_404

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
