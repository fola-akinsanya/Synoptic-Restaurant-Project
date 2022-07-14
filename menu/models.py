from django.db import models

# Create your models here.
class StarterMenu(models.Model):
    def ___str___(self):
        return self.title

    STARTERS = [
        ('Fried Calamari with Garlic & Chilli', 'Fried Calamari with Garlic & Chilli'),
        ('Burrata with Basil Pesto', 'Burrata with Basil Pesto'),
        ('No Starter', 'No Starter'),
        ('Bread', 'Bread')
    ]

    starter = models.CharField(max_length=100, choices= STARTERS)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
