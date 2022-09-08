from email.policy import default
from django.db import models

from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

from orders.models import Order

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
    
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cart_status = models.CharField(max_length=100, choices=STATUS, default='Order Received')
    cart_total = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    order_items = models.ManyToManyField(Order, related_name='cart')
