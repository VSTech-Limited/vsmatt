from .models import ProductCategory, JujaMall, BusinessCategory


def product_categories(request):
    return {"product_categories": ProductCategory.objects.all()}


def jujamall(request):
    return {'jujamall': JujaMall.objects.filter(set_current=True).first()}


def business_categories(request):
    return {'business_categories': BusinessCategory.objects.all()}
