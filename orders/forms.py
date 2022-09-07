from re import template
from tkinter import Widget
from django import forms
from menu.models import StarterMenu

from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django.forms import CheckboxSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit

from orders.models import Cart, StarterMenu

class MyOrderModelChoiceField(ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return f'({obj.starter} {obj.price})'

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'customer' in kwargs:
            self._customer = kwargs.pop('customer')
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post' # get or post
        self.helper.layout = Layout(
            Div('div_id_order_items', css_class="d-inline p-2 bg-primary text-white"),
        ) 

    order_items = MyOrderModelChoiceField(queryset=StarterMenu.objects.all(), widget = forms.CheckboxSelectMultiple)
    # order_items = forms.Select(choices=StarterMenu.objects.all())

    class Meta:
        model = Cart
        exclude = ['customer', 'order_status', 'order_total']
        fields = ['order_items']


    # def __init__(self, *args, **kwargs):
    #     if 'customer' in kwargs:
    #         self._customer = kwargs.pop('customer')
    #     super(OrderForm, self).__init__(*args, **kwargs)
            
    def save(self, commit=True):
        inst = super(OrderForm, self).save(commit=False)
        if  self._customer:
            inst.customer = self._customer
            
        if commit:
            inst.save()
            self.save_m2m()
        return inst

