from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.business),
    path('categories/<slug:slug>/', views.business, name='product_list_by_category'),
    path('business/', views.get_business, name='get'),

]
