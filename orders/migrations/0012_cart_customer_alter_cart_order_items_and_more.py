# Generated by Django 4.0.6 on 2022-07-14 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0004_alter_startermenu_starter'),
        ('orders', '0011_remove_starterorder_starter_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_items',
            field=models.ManyToManyField(related_name='cart', to='menu.startermenu'),
        ),
        migrations.DeleteModel(
            name='StarterOrder',
        ),
    ]