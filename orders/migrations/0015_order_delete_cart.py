# Generated by Django 4.0.6 on 2022-09-07 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0004_alter_startermenu_starter'),
        ('orders', '0014_remove_cart_order_items_cart_order_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Order Received', max_length=100)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order_items', models.ManyToManyField(related_name='order', to='menu.startermenu')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]