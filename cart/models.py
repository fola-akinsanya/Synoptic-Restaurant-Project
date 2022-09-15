from email.policy import default
from django.db import models

from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from orders.models import Order

class Cart(models.Model):
    def ___str___(self):
        return self.title
        
    STATUS = [
        ('Cart Created', 'Cart Created'),
        ('Order Received', 'Order Received'),
        ('Order Processing', 'Order Processing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ]
    
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cart_status = models.CharField(max_length=100, choices=STATUS, default='Cart Created')
    cart_total = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    order_items = models.ManyToManyField(Order, related_name='cart', null=True, blank=True)

class Checkout(models.Model):
    def __str__(self) -> str:
        return super().__str__()

    EXPIRY_MONTH = [
        (1, 1),
        (2, 2 ),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11), 
        (12, 12)
        ]

    EXPIRY_YEAR = [
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),
        (2025, 2025),
        (2026, 2026),
        (2027, 2027)
    ]   

    def validate_card_number_length(value):
        if len(str(value)) > 16:
            raise ValidationError(
                _('%(value)s is above 16 digits')
        )

    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    card_number = models.IntegerField(validators=[validate_card_number_length])
    card_expiry_month = models.IntegerField(choices=EXPIRY_MONTH)
    card_expiry_year = models.IntegerField(choices=EXPIRY_YEAR)
    billing_address = models.CharField(max_length=1000)
    delivery_address = models.CharField(max_length=1000)

