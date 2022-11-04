from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from business.models import BusinessBranch, BusinessProfile


def index(request, business_slug, branch_slug):
    business = get_object_or_404(BusinessProfile, slug=business_slug, owner=request.user)
    branch = get_object_or_404(BusinessBranch, slug=branch_slug, business__owner=request.user,
                               business=business)
    context = {
        'business': business,
        'branch': branch
    }
    return render(request, "farm/shop/index.html", context)



