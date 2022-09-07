from django.contrib import admin
from .models import Cart

# class OrdersInline(admin.TabularInline):
#     model = Cart.order_items.through

# class StarterOrderAdmin(admin.ModelAdmin):
#     inlines = (OrdersInline,)
#     list_display = ('customer', 'starter_order')
 
# admin.site.register(StarterOrder, StarterOrderAdmin)




class CartInline(admin.TabularInline):
    model = Cart.order_items.through

class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartInline,
    ]
    # exclude = ('order_items',)

admin.site.register(Cart, CartAdmin)



# class CartAdmin(admin.ModelAdmin):
#     list_display= ('customer', 'order_status', 'order_total', 'order_items')

# admin.site.register(Cart, CartAdmin)

