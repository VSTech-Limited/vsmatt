from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_view, name='products_list'),
    path('<slug:category_slug>/', views.products_view, name='category'),
    path('<slug:business_slug>/<slug:branch_slug>/', views.add_product, name='add'),
    path('<slug:business_slug>/<slug:branch_slug>/update/', views.update_product, name='update'),
    path('<slug:business_slug>/<slug:branch_slug>/delete/', views.delete_product, name='delete'),
]
