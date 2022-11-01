from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


# Create your views here.


def businesses(request, slug=None):
    return render(request, 'shop/business.html')


def business_index(request):
    return render(request, 'shop/business/index.html')




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
