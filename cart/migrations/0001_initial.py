# Generated by Django 4.0.6 on 2022-09-07 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0016_remove_order_order_status_remove_order_order_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Order Received', max_length=100)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('cart_items', models.ManyToManyField(related_name='cart', to='orders.order')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
