from django.contrib import admin
from .models import Cart

# Register your models here.

class CartInline(admin.TabularInline):
    model = Cart.order_items.through

class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartInline,
    ]

admin.site.register(Cart, CartAdmin)

