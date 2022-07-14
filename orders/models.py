from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from authlib.integrations.django_client import OAuth
from django.contrib.auth.models import User

from menu.models import StarterMenu

starter = tuple(StarterMenu.objects.values_list('starter', 'price'))

# Create your models here.

class StarterOrder(models.Model):
    def ___str___(self):
        return self.title

    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    starter_order = models.ForeignKey(StarterMenu, on_delete=models.CASCADE, null=True)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

class Cart(models.Model):
    def ___str___(self):
        return self.title
        
    STATUS = [
        ('Order Received', 'Order Received'),
        ('Order Processing', 'Order Processing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ]
    
    # customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_status = models.CharField(max_length=100, choices=STATUS)
    order_total = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    order_items = models.ManyToManyField(StarterOrder, related_name='carts')
    # starter_order = models.ForeignKey(StarterOrder, on_delete=models.CASCADE, null=True)

    # class Meta:
    #     ordering = ['customer']

    # def __str__(self):
    #     return self.customer

