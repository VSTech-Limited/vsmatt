from turtle import title
from django.shortcuts import render
from shop.models import BusinessProfile, BusinessBranch, Category
# Create your views here.
def index(request):
    bus = BusinessBranch.objects.all()
    categories = Category.objects.all()
    title = 'home'
    context ={
        'bus':bus,
        'title':title,
        'categories':categories,
    }
    #print(f"\n\n{title}\n\n")
    return render(request, 'index.html', context)

def about(request):
    title = 'About Us'
    context = {
        'title':title,
    }
    return render(request, 'about.html', context)

def contact(request):
    title = 'Contact us'
    context = {
        'title':title
    }
    return render(request, 'contact.html', context)

def products(request):
    title = 'Products'
    context = {
        'title':title
    }
    return render(request, 'products.html', context)