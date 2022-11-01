from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_view, name='products_list'),
]
