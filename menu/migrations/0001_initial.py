# Generated by Django 4.0.6 on 2022-07-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StarterMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starter', models.CharField(choices=[('garlic & chilli calamari', 'Fried calamari with garlic & chilli'), ('burrata with basil pesto', 'burrata with basil pesto')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
