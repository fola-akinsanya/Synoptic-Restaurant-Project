

# Create your tests here.

from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Booking

import datetime as dt


import datetime

class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        Booking.objects.create(customer=self.user)

    def test_database_interactions(self):
        self.client.login(username='testuser', password='12345')

        date = datetime.date.today()
        time = datetime.time(17,00)

        booking = Booking.objects.get(customer=self.user)
        print(booking.date)

        booking.date = date
        booking.save()
        booking.time = time
        booking.save()

        self.assertEqual(booking.date, date)
        self.assertEqual(booking.time, time)
