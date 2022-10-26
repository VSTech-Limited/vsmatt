from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.business),
    path('categories/<slug:slug>/', views.business, name='product_list_by_category'),
    path('business/', views.get_business, name='get'),
    path('business/register', views.register_business, name='register'),
    path('business/<int:bs_id>/branch/add', views.register_branch, name='register_branch'),
]
