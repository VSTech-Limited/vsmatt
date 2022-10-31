from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.business, name='business'),
    path('categories/<slug:slug>/', views.business, name='product_list_by_category'),
    path('business/categories/<slug:slug>/', views.businesses, name='business_list_by_category'),
    path('business/', views.get_business, name='get'),
    path('businesses/view/', views.business_list, name='businesses_list'),
    path('businesses/<int:bs_id>/<slug:bs_slug>/detailed/', views.business_detailed, name='business_detailed'),
    path('business/register', views.register_business, name='register_business'),
    path('business/<int:bs_id>/branch/add', views.register_branch, name='register_branch'),
    path('<slug:bs_slug>/<slug:br_slug>/product/add', views.register_branch, name='register_branch'),

    # when changing url don't change bellow
    path("<int:business_id>/<int:branch_id>/<slug:branch_slug>/", views.view_business_products)
]
