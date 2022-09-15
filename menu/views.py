from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import redirect, render, redirect
from django.contrib.auth.decorators import login_required
from menu.forms import MenuForm

from cart.forms import CartForm

# Create your views here.
@login_required
def menu(request):

    if request.method == "POST":
        menu_form = MenuForm(request.POST)

        if menu_form.is_valid():
            menu_form.save()
            return redirect("menu")
    else:
        context = {
        'menu_form': MenuForm(),
        }
        
        return render (request, "menu.html", context)
