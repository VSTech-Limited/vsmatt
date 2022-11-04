from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request, business_slug, branch_slug):
    return render(request, "farm/shop/index.html")



