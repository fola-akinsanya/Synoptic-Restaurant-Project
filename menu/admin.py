from tkinter import Menu
from django.contrib import admin

from orders.admin import OrderInline
from .models import StarterMenu

# Register your models here.
class StarterMenuAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    
    list_display = ('starter', 'price')
 
admin.site.register(StarterMenu, StarterMenuAdmin)