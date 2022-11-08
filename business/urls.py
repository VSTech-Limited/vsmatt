from django.urls import path, include
from . import views
from shop.views import index

app_name = 'business'
urlpatterns = [
    path('', views.businesses, name='businesses'),
    path('categories/<slug:category_slug>/', views.businesses, name='category'),
    path('own/<slug:business_slug>/delete/', views.delete_business, name='business_delete'),
    path('own/<slug:business_slug>/update/', views.update_business, name='business_update'),
    path('<slug:business_slug>/<slug:branch_slug>/delete/', views.delete_branch, name='branch_delete'),
    path('<slug:business_slug>/<slug:branch_slug>/update/', views.update_branch, name='branch_update'),
    path('register/', views.register_business, name='register_business'),
    path('<slug:business_slug>/branch/add/', views.register_branch, name='register_branch'),
    path('own/', views.own_businesses_list, name='own_business_list'),
    path('own/<slug:business_slug>/', views.own_business_detailed, name='own_business_detailed'),
    path('orders/', views.orders, name='orders'),
]
