from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import BusinessProfile


# Create your views here.

@csrf_exempt
def business(request):
    bus = BusinessProfile.objects.all()
    return render(request, 'shop/business.html', {'bus': bus})
