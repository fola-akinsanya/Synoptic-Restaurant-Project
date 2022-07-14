from django.shortcuts import render

import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart

from orders.forms import StarterOrderForm

# Create your views here.
def index(request):
    return render(
        request,
        "index.html", 
        {'user': request.user}
    )
@login_required
def starter_order(request):

    if request.method == "POST":
        print (request.POST)
        starter_order_form = StarterOrderForm(request.POST, customer= request.user)

        if starter_order_form.is_valid():
            starter_order_form.save()
            print (starter_order_form)
        return redirect("index")
    else:
        context = {
        'starter_order_form':StarterOrderForm()
    }
        starter_order_form = StarterOrderForm()
    return render (request, "order.html", context)

def cart(request):
    cart = Cart.objects.annotate(
        price=Sum(F('order_items__price'))
    ).get(
       customer=request.user
    )
    cart.total = cart.price
    cart.save()

# def cart (request):
#     cart = Cart.objects.filter(customer=request.user)
#     total = 0 
#     for i in cart:
#         total = i.order_items.price