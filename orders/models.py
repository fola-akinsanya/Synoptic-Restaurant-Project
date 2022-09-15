from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

from menu.models import MainMenu

class Order(models.Model):
    def ___str___(self):
        return self.title
        
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_items = models.ManyToManyField(MainMenu, related_name='order')
