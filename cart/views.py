from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import redirect, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Cart

# Create your views here.
def index(request):
    return render(
        request,
        "index.html", 
        {'user': request.user}
    )

@login_required
def cart(request):
    if request.method == "GET":
        # order_items = prefetch_related_objects(Cart, 'order_items')
        # user_carts = Order.objects.filter(customer=request.user).filter(order_items__isnull=False).prefetch_related("order_items")
        user_cart = Cart.objects.get(customer=request.user)

        orders = [list(order.order_items.all() for order in user_cart.order_items.all())]

        starters = []
        cart_total = 0
        
        for o in orders:
            for i in o:
                starters += i.all()
                print(starters)
                for price in i:
                    cart_total += price.price

        context = {
            'cart': user_cart,
            'orders': orders,
            'starter': starters,
            'cart_total': cart_total
        }

        return render (request, "cart.html", context)
