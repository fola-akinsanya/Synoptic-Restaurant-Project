from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import EditProfileForm

from cart.models import Cart
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def index(request):
    return render(
        request,
        "index.html", 
        {'user': request.user}
    )

def register_view(request):
	if request.method == "POST":
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			new_user= register_form.save()
			new_user = register_form.save()
			#messages.info(request, "Thanks for registering. You are now logged in.")
			new_user = authenticate(username=register_form.cleaned_data['username'],
            	password=register_form.cleaned_data['password1'],
            	)
			login(request, new_user)
			new_cart = Cart(customer=request.user)
			new_cart.save()

			return redirect("index")
	else:
		register_form = RegisterForm()
		

	return render(request, "registration/register.html", {"register_form":register_form })

def logout_view(request):
    logout(request)
    return redirect("index")

def edit_profile_view(request):
	if request.method =="POST":
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
		form = EditProfileForm(instance=request.user)
		return render(request, 'registration/edit_profile.html', {'form':form})

def change_password_view(request):
	if request.method =="POST":
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('registration/passwordchangesuccess.html')

	else:
		form = PasswordChangeForm(user=request.user)
		return render(request, 'registration/change_password.html', {'form':form})

def profile(request):
	if request.method == "GET":
		return render (request, "registration/profile.html")

def contact_us(request):
	if request.method == "GET":
		return render (request, "contact_us.html")
