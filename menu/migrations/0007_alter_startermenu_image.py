# Generated by Django 4.0.6 on 2022-09-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_startermenu_image_height_startermenu_image_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startermenu',
            name='image',
            field=models.ImageField(blank=True, default='media/bread.jpeg', height_field='image_height', null=True, upload_to='', width_field='image_width'),
        ),
    ]