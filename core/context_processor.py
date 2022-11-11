from .models import JujaMall


def jujamall(request):
    return {'vsmatt': JujaMall.objects.filter(set_current=True).first()}
