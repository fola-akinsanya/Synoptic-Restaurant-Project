from django.shortcuts import render

from django.shortcuts import redirect, render, redirect
from django.contrib.auth.decorators import login_required
from cart.forms import CartForm
from cart.models import Cart
from menu.models import MainMenu
from menu.views import menu

from orders.forms import OrderForm
from orders.models import Order
from cart.forms import CartForm

# Create your views here.
@login_required
def order(request):

    if request.method == "POST":
        order_form = OrderForm(request.POST, customer= request.user)

        if order_form.is_valid():

            order_form.save()
            orders = Order.objects.filter(customer=request.user)
            
            cart = Cart.objects.get(customer=request.user)
            cart.order_items.set(orders)
            cart.save()

            for item in order_form.cleaned_data["order_items"]:
                menu_item = MainMenu.objects.get(id=item.pk)
                menu_item.stock -= 1
                menu_item.save()

            return redirect("cart")

    else:
        context = {
        'order_form': OrderForm(),
        }
        
        return render (request, "order.html", context)
