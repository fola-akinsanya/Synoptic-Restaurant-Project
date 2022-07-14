from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
	
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2',]

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email', 'password']

	def __init__(self, *args, **kwargs):
		super(UserChangeForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password'].help_text= "Click <a href=\"../change_password\"> Here</a> to change your Password."




 

