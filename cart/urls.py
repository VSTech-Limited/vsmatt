from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('process/', views.process_cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('detail/', views.view_detailed, name='view_cart_detail'),
    path('shipping/details/', views.shipping_details, name='shipping_details'),
    # path('payment/options/', views.payment_options, name='payment_options'),
]