from audioop import reverse
from email.mime import image
from re import template
from tkinter import Label, Widget
from django import forms
from menu.models import MainMenu

from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django.forms import CheckboxSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit, MultiWidgetField
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe


from orders.models import Order, MainMenu

class MyOrderModelChoiceField(ModelMultipleChoiceField):

    @mark_safe
    def label_from_instance(self, obj):

        if obj.stock > 0:
            return (f'{obj.menu_item} £{obj.price}')
            # return (f'{obj.menu_item} {obj.price}' "<img src='%s'/>" % obj.image.url)

        else:
            obj.price == 0
            return (f'{obj.menu_item} SOLD OUT')

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'customer' in kwargs:
            self._customer = kwargs.pop('customer')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST' # get or post
        self.helper.add_input(Submit('submit', 'Add to basket'))
        # self.helper.layout = Layout(
        #     Field('order_items', wrapper_class="form-check"),
        # )
            # Label('order_items', attrs= ({
            #     'id': 'id_order_items_3',
            #     'class': 'form-check-label'
            # }))
            # MultiWidgetField(
            # 'order_items',
            # attrs=(
            #     {'style': 'width: 20px;'},
            #     {'class': 'form-check-input'}
            # ),
        # )
        #     Field(css_class="form-check"),
        # ) 


    order_items = MyOrderModelChoiceField(queryset=MainMenu.objects.all(), widget = forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    # order_items = forms.Select(choices=StarterMenu.objects.all())

    class Meta:
        model = Order
        exclude = ['customer']
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
