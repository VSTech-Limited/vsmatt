from products.models import ProductCategory


def product_categories(request):
    return {"product_categories": ProductCategory.objects.all()}
