from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('<slug:business_slug>/<slug:branch_slug>/', views.index, name='shop'),
]
