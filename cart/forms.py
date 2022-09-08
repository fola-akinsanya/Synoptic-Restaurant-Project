from re import template
from tkinter import Widget
from django import forms
from menu.models import StarterMenu

from django.forms import ModelMultipleChoiceField


from .models import Cart
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
