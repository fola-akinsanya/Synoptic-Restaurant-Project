from django.shortcuts import render

from django.shortcuts import redirect, render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import prefetch_related_objects
from menu.models import StarterMenu

from orders.forms import OrderForm
from orders.models import Cart

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
        print (request.POST)
        order_form = OrderForm(request.POST, customer= request.user)

        if order_form.is_valid():
            order_form.save()
            print (order_form)
        return redirect("cart")
    else:
        context = {
        'order_form': OrderForm(),
        'fola': 'Fola'
        }
    return render (request, "order.html", context)

@login_required
def cart(request):
    if request.method == "GET":
        # order_items = prefetch_related_objects(Cart, 'order_items')
        user_carts = Cart.objects.filter(customer=request.user).filter(order_items__isnull=False).prefetch_related("order_items")
        # orders = [list(order.order_items) for order in cart]
        # i = 0
        # while i < len(cart):
        #     cart[i].order_items.set(cart[i].order_items.all())
        #     i += 1

        orders = [list(cart.order_items.all() for cart in user_carts)]

        all_orders = [o for o in orders]

        starter_order = [i for i in all_orders]

        starter_order2 = [j  for j in starter_order]
        
        for o in orders:
            for i in o:
                starter = i.all()

        context = {
            'cart': cart,
            'orders': orders,
            'starter': starter
        }
        # print (user_carts[9].order_items.all())
        # print (dir(orders[0]))
        # print (all_orders)
        # print (starter_order)




        # print (str(starter_order2))

        # for display list of orders, append to starter_menu.starter list

        # for o in orders:
        #     print("o column" + str(o))
        #     for i in o:
        #         print("i column" + str(i.all()))
        #         for starter_menu in i.all():
        #             print(starter_menu.starter)
        return render (request, "cart.html", context)

# def cart(request):
#     cart = Cart.objects.annotate(
#         price=Sum(F('order_items__price'))
#     ).get(
#        customer=request.user
#     )
#     cart.total = cart.price
#     cart.save()

# def cart (request):
#     cart = Cart.objects.filter(customer=request.user)
#     total = 0 
#     for i in cart:
#         total = i.order_items.price