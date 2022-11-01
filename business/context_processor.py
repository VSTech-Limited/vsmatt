from .models import BusinessCategory


def business_categories(request):
    return {'business_categories': BusinessCategory.objects.all()}