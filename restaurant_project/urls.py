"""restaurant_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from menu.views import menu

# not for prod
from django.conf.urls.static import static 
from django.conf import settings


from user.views import userPageView
from orders.views import order
from cart.views import cart, checkout, delete_order, checkout, order_received, active_orders
from menu.views import menu
from booking.views import active_order_exists, booking, booking_requested
from register.views import contact_us, register_view, login, change_password_view, edit_profile_view, profile, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user", userPageView, name="home"),
    path("", index, name="index"),
    path("login", auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name= "login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register", register_view, name="register"),
    path("order", order, name="order"),
    path("cart", cart, name="cart"),
    path("menu", menu, name="menu"),
    path("delete-order/<order_id>/<menu_item_id>", delete_order, name="delete-order"),
    path("change-password", change_password_view, name="change-password"),
    path("edit-profile", edit_profile_view, name="edit-profile"),
    path("profile", profile, name="profile"),
    path("checkout", checkout, name="checkout"),
    path("order-received", order_received, name="order-received"),
    path("active-orders", active_orders, name='active-orders'),
    path("contact-us", contact_us, name='contact-us'),
    path("book-table", booking, name="booking"),
    path("booking-requested", booking_requested, name="booking-requested"),
    path("active-order-exists", active_order_exists, name="active-order-exists")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
