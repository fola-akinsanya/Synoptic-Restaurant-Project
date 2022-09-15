from re import template
from tkinter import Widget
from django import forms
from menu.models import MainMenu

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.forms import ModelMultipleChoiceField


from .models import Cart, Checkout
from orders.models import Order

class CartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'customer' in kwargs:
            self._customer = kwargs.pop('customer')
        super(CartForm, self).__init__(*args, **kwargs)

    order_items = ModelMultipleChoiceField(queryset=Order.objects.all())

    class Meta:
        model = Cart
        fields = ['customer', 'cart_status', 'cart_total', 'order_items']
            
    def save(self, commit=True):
        inst = super(CartForm, self).save(commit=False)
        if  self._customer:
            inst.customer = self._customer
            
        if commit:
            inst.save()
            self.save_m2m()
        return inst

class CheckoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'customer' in kwargs and 'cart' in kwargs:
            self._customer = kwargs.pop('customer')
            self._cart = kwargs.pop('cart')

        # if 'cart' in kwargs:
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Pay Now'))

    class Meta:
            model = Checkout
            exclude = ['customer', 'cart']
            fields = ['name', 'card_number', 'card_expiry_month', 'card_expiry_year', 'billing_address', 'delivery_address']

    def save(self, commit=True):
        inst = super(CheckoutForm, self).save(commit=False)
        if  self._customer and self._cart:
            inst.customer = self._customer
            inst.cart = self._cart

            
        if commit:
            inst.save()
            self.save_m2m()
        return inst
