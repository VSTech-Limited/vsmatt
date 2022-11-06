from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.shortcuts import reverse

from cart.cart import Cart
from order.models import OrderItem, Order


def order_create(request):
    cart = Cart(request)
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
        return render(
            request,
            'farm/order/created.html',
            {
                'order': order
            }
        )
    return redirect('products:products_list')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/order_history.html', {'orders': orders})


@login_required
def view_order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    return render(request, 'order/order_details.html', {"order": order})


@login_required
def order_payment_history(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "order/payment_history.html", {"order": order})


def view_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order/pdf.html', {"order": order})
