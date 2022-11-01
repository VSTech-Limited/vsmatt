from .models import JujaMall


def jujamall(request):
    return {'jujamall': JujaMall.objects.filter(set_current=True).first()}
