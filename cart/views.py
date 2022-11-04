from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from products.models import Product


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    else:
        print("VALIDATION ERROR")
    # cart.remove(product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def process_cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })

    return redirect("shop:product_list")


def view_detailed(request):
    return render(request, 'cart/detailed.html')


def shipping_details(request):
    # user_form = UserEditForm(instance=request.user)
    # profile_form = UserProfileInfo(instance=request.user.userprofile)
    # residential_info_form = ResidentialInfoForm(instance=request.user.residentialinfo)

    # if request.method == 'POST':
    #     residential_info_form = ResidentialInfoForm(data=request.POST, instance=request.user.residentialinfo)
    #     profile_form = UserProfileInfo(data=request.POST, instance=request.user.userprofile)
    #     user_form = UserEditForm(instance=request.user, data=request.POST)
    #
    #     if residential_info_form.is_valid() and profile_form.is_valid() and user_form.is_valid():
    #         residential_info_form.save()
    #         profile_form.save()
    #         user_form.save()
    #         return redirect('order:order_create')

    return render(
        request,
        'cart/shipping_details.html',
        {
            # 'residential_info_form': residential_info_form,
            # 'user_form': user_form,
            # 'profile_form': profile_form,
            # 'bread_crumb': bread_crumb
        }
    )

