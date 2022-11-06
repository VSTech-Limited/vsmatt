# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

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
    return render(request, 'farm/order/order_history.html', {'orders': orders})


@login_required
def view_order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    return render(request, 'farm/order/order_details.html', {"order": order})


@login_required
def order_payment_history(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "farm/order/payment_history.html", {"order": order})


def view_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'farm/order/pdf.html', {"order": order})
