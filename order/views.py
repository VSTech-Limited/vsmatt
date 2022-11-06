# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from cart.cart import Cart
from cart.session_info import SessionInfo
from order.models import OrderItem, Order


def order_create(request):
    cart = Cart(request)
    session = SessionInfo(request)
    if len(cart):
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        # clear the cart
        cart.clear()
        session.remove("branch")
        messages.success(request, "Your order has been placed successfully!")
        return redirect(reverse(
            'order:order_details',
            args=[order.id]
        ))
    messages.warning(request, "Cant place an order on an empty cart!")
    return redirect('cart:shipping_details')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'farm/order/order_history.html', {'orders': orders})


@login_required
def view_order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'farm/order/detailed.html', {"order": order})


def view_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'farm/order/invoice.html', {"order": order})
