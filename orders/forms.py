from django import forms
from menu.models import StarterMenu

from django.forms import ModelChoiceField

from orders.models import StarterOrder

class MyStarterModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return f'({obj.starter} {obj.price})'

class StarterOrderForm(forms.ModelForm):
    starter_order = MyStarterModelChoiceField(queryset=StarterMenu.objects.all())
    
    class Meta:
        model = StarterOrder
        exclude = ['customer']
        widgets = {
            'starter_order': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        if 'customer' in kwargs:
            self._customer = kwargs.pop('customer')
        super(StarterOrderForm, self).__init__(*args, **kwargs)
            
    def save(self, commit=True):
        inst = super(StarterOrderForm, self).save(commit=False)
        if  self._customer:
            inst.customer = self._customer
            
        if commit:
            inst.save()
            self.save_m2m()
        return inst