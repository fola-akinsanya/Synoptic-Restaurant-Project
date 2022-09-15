
# Create your views here.
from django.shortcuts import redirect, render

from .models import Cart, Checkout
from orders.models import Order
from menu.models import MainMenu
from .forms import CheckoutForm

def cart(request):

    if request.method == "GET":
        try:
            user_cart = Cart.objects.get(customer=request.user)
            orders = [order for order in user_cart.order_items.all()]
        
            cart_total = 0


            for o in orders:
                for i in o.order_items.all():
                    print(o.order_items.all())
                    cart_total += i.price
        
            user_cart.cart_total = cart_total
            user_cart.save()

            context = {
                'cart': user_cart,
                'orders': orders,
                'cart_total': cart_total,
            }
            return render (request, "cart.html", context)
     
        except:
            cart_total = 0
            context = {
                'cart_total': cart_total,
            }
            return render (request, "cart.html", context)


def delete_order(request, order_id, menu_item_id):
    user_cart = Cart.objects.get(customer=request.user)
   
    menu_item = Order.objects.get(pk=order_id).order_items.get(pk=menu_item_id)        
        
    order = Order.objects.get(pk=order_id)

    order.order_items.remove(menu_item)
    menu_item.stock +=1
    menu_item.save()
    
    if order.order_items.exists():
        pass
    else:
        del order

    return redirect ('cart')

def checkout(request):
    
    if request.method == "POST":
        user_cart = Cart.objects.get(customer=request.user)
        checkout_form = CheckoutForm(request.POST, customer= request.user, cart=user_cart)

        try: 
            if checkout_form.is_valid():
                checkout_form.save()            
                user_cart.cart_status = "Order Received"
                user_cart.save()

                return redirect("order-received")
        except:
                return redirect("active-order-exists")

    context = {   
        'cart': Cart.objects.get(customer=request.user),
        'checkout_form': CheckoutForm(),
    }
        
    return render (request, "checkout.html", context)

def order_received(request):

    return render(
        request,
        "order_received.html", 
        {'user': request.user}
    )

def active_orders(request):
    try: 
        checkout = Checkout.objects.get(customer=request.user)
    except: 
        checkout = 0
    
    user_cart = Cart.objects.get(customer=request.user)
    orders = [order for order in user_cart.order_items.all()]

    context = {
        'checkout': checkout,
        'cart': user_cart,
        'orders': orders
    }
    return render(
        request,
        "active_orders.html", 
        context
    )