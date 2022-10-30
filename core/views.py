from django.shortcuts import render, redirect
from core.forms import ContactForm
from core.models import Team
from shop.models import BusinessProfile, BusinessBranch, ProductCategory
from django.contrib import messages

# Create your views here.
def index(request):
    business_branch = BusinessBranch.objects.all()
    title = 'home'
    context = {
        'title': title,
        'business_branch': business_branch
    }
    # print(f"\n\n{title}\n\n")
    return render(request, 'index.html', context)


def about(request):
    title = 'About Us'
    team = Team.objects.all()
    context = {
        'title': title,
        'team': team
    }
    return render(request, 'about.html', context)


def contact(request):
    title = 'Contact us'
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect('index')

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'contact.html', context)


def products(request):
    title = 'Products'
    categories = ProductCategory.objects.all()
    context = {
        'title': title,
        'categories': categories,
    }
    return render(request, 'products.html', context)

def faq(request):
    title = 'FAQ'
    context = {
        'title': title,
    }
    return render(request, 'faq.html', context)
