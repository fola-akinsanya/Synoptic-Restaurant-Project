from django import forms
from .models import StarterMenu

class StarterOrderForm(forms.ModelForm):
    class Meta:
        model = StarterMenu
        fields = ('starter',)

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