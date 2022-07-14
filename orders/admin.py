from django.contrib import admin
from .models import Cart, StarterOrder

# Register your models here.

# class CartAdmin(admin.ModelAdmin):
#     list_display = ( 'order_items', 'order_status', 'order_total')
#     admin.site.register(Cart, CartAdmin)

# class CartInline(admin.TabularInline):
#     model = StarterOrder.starter_order.through

class OrdersInline(admin.TabularInline):
    model = Cart.order_items.through

# admin.site.register(Cart, OrdersInline)

class StarterOrderAdmin(admin.ModelAdmin):
    inlines = (OrdersInline,)
    list_display = ('customer', 'starter_order')
 
admin.site.register(StarterOrder, StarterOrderAdmin)

class CartAdmin(admin.ModelAdmin):
    inlines = [
        OrdersInline,
    ]
    exclude: ('order_items,')

admin.site.register(Cart, CartAdmin)

