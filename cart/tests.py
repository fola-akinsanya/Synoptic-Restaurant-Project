from email.mime import image
from tkinter import StringVar
from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Cart
from orders.models import Order
from menu.models import MainMenu

class CartTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        MainMenu.objects.create(menu_item='Fried Calamari with Garlic & Chilli', price=8, stock=10)
        Cart.objects.create(customer=self.user)
        Order.objects.create(customer=self.user)

    def test_database_interactions(self):
        self.client.login(username='testuser', password='12345')

        """update/read --- many to many relationships- order is made up of menus and cart is made up of orders"""
        menu = MainMenu.objects.get(pk=1)
        cart = Cart.objects.get(customer=self.user)

        order = Order.objects.get(pk=1)
        order.order_items.set([menu])
        order.save()

        cart.order_items.set([order])
        cart.save()
        # self.assertEqual(order.order_items, menu)
        self.assertEqual(cart.order_items.get(), order)
        self.assertEqual(order.order_items.get(), menu)

        """create -- objects are added in database with expected defaults"""

        self.assertEqual(cart.cart_status, "Cart Created")
        self.assertEqual(cart.cart_total, 0)
        self.assertEqual(cart.order_items.count(), 1)

        """delete -- objects are deleted in database and in their respective many to many relationships"""

        menu.delete()
        self.assertFalse(order.order_items.count())
        
        order.delete()
        self.assertFalse(cart.order_items.count())

