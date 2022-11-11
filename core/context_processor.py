from .models import vsmatt


def vsmatt(request):
    return {'vsmatt': vsmatt.objects.filter(set_current=True).first()}
