# Generated by Django 4.0.6 on 2022-07-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_startermenu_starter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startermenu',
            name='starter',
            field=models.CharField(choices=[('Fried Calamari with Garlic & Chilli', 'Fried Calamari with Garlic & Chilli'), ('Burrata with Basil Pesto', 'Burrata with Basil Pesto'), ('No Starter', 'No Starter'), ('Bread', 'Bread')], max_length=100),
        ),
    ]
