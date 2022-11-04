from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('<slug:business_slug>/<slug:branch_slug>/', views.index, name='shop'),
    path('<slug:business_slug>/<slug:branch_slug>/products/list/', views.products_list, name='product_list'),
    path('<slug:business_slug>/<slug:branch_slug>/<slug:category_slug>/list/', views.products_list, name='category'),
    path('<slug:business_slug>/<slug:branch_slug>/<slug:product_slug>/detail/', views.product_detailed, name='product_detail'),
]
