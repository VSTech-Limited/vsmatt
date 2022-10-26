from .models import Category, JujaMall


def categories(request):
    return {"categories": Category.objects.all()}


def jujamall(request):
    return {'jujamall': JujaMall.objects.filter(set_current=True).first()}
