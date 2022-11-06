from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('history/', views.order_history, name='order_history'),
    path('<int:order_id>/', views.view_order_details, name='order_details'),
    path('<int:order_id>/invoice', views.view_invoice, name='order_invoice'),
    path('<int:order_id>/payment/history', views.order_payment_history, name='order_payment_history'),
]