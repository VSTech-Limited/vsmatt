from .models import VSMatt


def vsmatt(request):
    return {'VSMatt': VSMatt.objects.filter(set_current=True).first()}
