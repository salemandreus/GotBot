# Generated by Django 5.0.1 on 2024-01-24 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_stock_refilled_stock_refilled_by'),
        ('supplyitems', '0007_rename_supplyitems_supplyitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='supplyitems.supplyitem'),
        ),
    ]
