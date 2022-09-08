from django.contrib import admin
from .models import Order
from cart.admin import CartInline

class OrderInline(admin.TabularInline):
    model = Order.order_items.through

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        CartInline,
    ]
     
admin.site.register(Order, OrderAdmin)

# class CartAdmin(admin.ModelAdmin):
#     list_display= ('customer', 'order_status', 'order_total', 'order_items')

# admin.site.register(Cart, CartAdmin)

