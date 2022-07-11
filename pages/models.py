from django.db import models
from authlib.integrations.django_client import OAuth
from django.contrib.auth.models import User

oauth = OAuth()

# Create your models here.
class StarterMenu(models.Model):
    def ___str___(self):
        return self.title

    STARTERS = [
        ('garlic & chilli calamari', 'Fried calamari with garlic & chilli'),
        ('burrata with basil pesto', 'burrata with basil pesto')
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    starter = models.CharField(max_length=100, choices= STARTERS)

