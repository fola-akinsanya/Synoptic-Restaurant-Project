# Generated by Django 4.0.6 on 2022-09-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_mainmenu_delete_startermenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='menu_item',
            field=models.CharField(choices=[('Fried Calamari with Garlic & Chilli', 'Fried Calamari with Garlic & Chilli'), ('Burrata with Basil Pesto', 'Burrata with Basil Pesto'), ('Roasted aubergine', 'Roasted aubergine'), ('Bread', 'Bread'), ('Grilled sea bass with roasted vegetables', 'Grilled sea bass with roasted vegetables'), ('Classic Burger', 'Classic Burger'), ('Seafood linguine', 'Seafood linguine'), ('Lobster bisque', 'Lobster bisque')], max_length=100),
        ),
    ]
