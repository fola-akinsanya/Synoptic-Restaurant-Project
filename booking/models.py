from datetime import datetime
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):

    import datetime as dt

    GUESTS = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6)
    ]
        
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    guests= models.SmallIntegerField(choices=GUESTS)
    date = models.DateField(null=True)
    time = models.TimeField(default=dt.time(00, 00))
