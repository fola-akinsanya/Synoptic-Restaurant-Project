from audioop import reverse
from re import template
from tkinter import Widget
from django import forms
from menu.models import MainMenu

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from orders.models import MainMenu

class MenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'GET'
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = MainMenu
        fields = ['menu_item', 'price', 'image']


            
    def save(self, commit=True):
        inst = super().save(commit=False)
        if  self._customer:
            inst.customer = self._customer
            
        if commit:
            inst.save()
            self.save_m2m()
        return inst
