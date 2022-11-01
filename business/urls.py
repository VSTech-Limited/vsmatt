from django.urls import path
from . import views

app_name = 'business'
urlpatterns = [

    path('', views.businesses, name='all_businesses_list'),
    path('categories/<slug:category_slug>/', views.businesses, name='category_business_list'),
    path('register/', views.register_business, name='register_business'),
    path('<slug:business_slug>/branch/add/', views.register_branch, name='register_branch'),
    path('own/', views.own_businesses_list, name='own_business_list'),
    path('own/<slug:business_slug>/', views.own_business_detailed, name='own_business_detailed'),
    path("own/<slug:business_slug>/<slug:branch_slug>/", views.own_business_branch_detailed)
]
