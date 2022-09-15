from django.contrib import admin
from .models import Cart, Checkout

# Register your models here.

class CartInline(admin.TabularInline):
    model = Cart.order_items.through

class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartInline,
    ]

admin.site.register(Cart, CartAdmin)

class CheckoutAdmin(admin.ModelAdmin):
    model = Checkout
    
    fields = ['customer', 'cart', 'name', 'card_number', 'card_expiry_month', 'card_expiry_year', 'billing_address']

admin.site.register(Checkout, CheckoutAdmin)

