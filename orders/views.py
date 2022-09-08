from django.shortcuts import render

from django.shortcuts import redirect, render, redirect
from django.contrib.auth.decorators import login_required
from cart.forms import CartForm
from cart.models import Cart

from orders.forms import OrderForm
from orders.models import Order
from cart.forms import CartForm

# Create your views here.
def index(request):
    return render(
        request,
        "index.html", 
        {'user': request.user}
    )
@login_required
def order(request):

    if request.method == "POST":
        order_form = OrderForm(request.POST, customer= request.user)

        if order_form.is_valid():
            order_form.save()
            orders = Order.objects.filter(customer=request.user)
            # cart = Cart.objects.get(customer=request.user)
            try:
                cart = Cart.objects.get(customer=request.user)
                cart.save()
                cart.order_items.set(orders)
                cart.save()
                return redirect("cart")
            # if not (Cart.objects.get(customer=request.user)):
            #     order_form.save()
            #     new_cart = Cart(customer=request.user)
            #     new_cart.save()
            #     new_cart.order_items.set(order_form.order_items)
            #     new_cart.save()
            #     return redirect("cart")
            # else:
            #     cart = Cart.objects.get(customer=request.user)
            #     cart.order_items.set(orders)
            except Cart.DoesNotExist:
                new_cart = Cart(customer=request.user)
                new_cart.save()
                new_cart.order_items.set(order_form.order_items)
                new_cart.save()
                return redirect("cart")
    else:
        context = {
        'order_form': OrderForm(),
        }
        
        return render (request, "order.html", context)
