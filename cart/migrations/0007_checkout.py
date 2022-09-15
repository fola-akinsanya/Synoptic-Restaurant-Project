# Generated by Django 4.0.6 on 2022-09-13 16:54

import cart.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0006_rename_cart_items_cart_order_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('card_number', models.IntegerField(validators=[cart.models.Checkout.validate_card_number_length])),
                ('card_expiry_month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('card_expiry_year', models.IntegerField(choices=[(2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027)])),
                ('billing_address', models.CharField(max_length=1000)),
                ('cart', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]