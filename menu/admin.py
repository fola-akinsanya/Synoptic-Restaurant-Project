from tkinter import Menu
from django.contrib import admin
from .models import StarterMenu

# Register your models here.
class StarterMenuAdmin(admin.ModelAdmin):
	list_display = ('starter', 'price')
 
admin.site.register(StarterMenu, StarterMenuAdmin)