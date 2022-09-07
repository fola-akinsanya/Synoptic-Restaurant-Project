# Generated by Django 4.0.6 on 2022-07-14 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_startermenu_starter'),
        ('orders', '0012_cart_customer_alter_cart_order_items_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order_items',
        ),
        migrations.AddField(
            model_name='cart',
            name='order_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.startermenu'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_status',
            field=models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Order Received', max_length=100),
        ),
    ]
