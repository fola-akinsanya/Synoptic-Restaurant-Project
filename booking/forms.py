from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

import datetime as dt
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]


class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'customer' in kwargs:
            self._customer = kwargs.pop('customer')
        super(BookingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST' # get or post
        self.helper.add_input(Submit('submit', 'Request Booking'))
    

    class Meta:
        model = Booking
        exclude = ['customer']
        fields = ['date', 'time', 'guests']


        widgets = {'time': forms.Select(choices=HOUR_CHOICES), 'date': forms.DateInput(attrs={'type': 'date'})}
    
    def save(self, commit=True):
        inst = super(BookingForm, self).save(commit=False)
        if  self._customer:
            inst.customer = self._customer
            
        if commit:
            inst.save()
            self.save_m2m()
        return inst
