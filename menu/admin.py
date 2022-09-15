from tkinter import Menu
from django.contrib import admin

from orders.admin import OrderInline
from .models import MainMenu

# Register your models here.
class MainMenuAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    
    list_display = ('menu_item', 'price', 'image', 'stock')
 
admin.site.register(MainMenu, MainMenuAdmin)