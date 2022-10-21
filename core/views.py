from django.shortcuts import render
from shop.models import BusinessProfile, BusinessBranch
# Create your views here.
def index(request):
    bus = BusinessBranch.objects.all()

    context ={
        'bus':bus
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')