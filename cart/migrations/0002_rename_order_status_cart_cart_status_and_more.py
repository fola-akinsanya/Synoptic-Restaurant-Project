# Generated by Django 4.0.6 on 2022-09-07 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='order_status',
            new_name='cart_status',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='order_total',
            new_name='cart_total',
        ),
    ]
