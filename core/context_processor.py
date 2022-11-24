from .models import Vsmatt


def vsmatt(request):
    return {'vsmatt': Vsmatt.objects.filter(set_current=True).first()}
