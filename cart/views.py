from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_POST

from business.models import BusinessBranch
from users.forms import UserEditForm, UserProfileInfo
from .cart import Cart
from .forms import CartAddProductForm
from .session_info import SessionInfo
from products.models import Product


@require_POST
def cart_add(request, product_id, branch_id=None):
    cart = Cart(request)
    session = SessionInfo(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    # add current branch to session if if on update to allow redirect to the last shop products list
    if branch_id:
        session.add({'branch': branch_id})
    # cart.remove(product)
    return redirect('cart:view_cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:view_cart_detail')


def process_cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })

    return redirect("shop:product_list")


def resume_shop(request):
    session = SessionInfo(request)
    branch_id = session.pop("branch")
    if branch_id:
        branch = get_object_or_404(BusinessBranch, id=branch_id)
        return redirect(reverse(
            'shop:product_list',
            args=[
                branch.business.slug,
                branch.slug,

            ]
        ))
    else:
        return redirect("products:products_list")


def view_detailed(request):
    cart = Cart(request)
    # branch_id = cart.getExtra("branch")
    # if branch_id:
    #     branch = get_object_or_404(BusinessBranch, id=branch_id)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    return render(request, 'farm/cart/detail.html')


@login_required
def shipping_details(request):
    user_form = UserEditForm(instance=request.user)
    profile_form = UserProfileInfo(instance=request.user.profile)
    # residential_info_form = ResidentialInfoForm(instance=request.user.residentialinfo)

    if request.method == 'POST':
        profile_form = UserProfileInfo(data=request.POST, instance=request.user.profile)
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('order:order_create')

    return render(
        request,
        'farm/cart/shipping_details.html',
        {
            # 'residential_info_form': residential_info_form,
            'user_form': user_form,
            'profile_form': profile_form,
            # 'bread_crumb': bread_crumb
        }
    )
