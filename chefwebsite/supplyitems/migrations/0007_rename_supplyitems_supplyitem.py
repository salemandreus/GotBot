# Generated by Django 5.0.1 on 2024-01-24 16:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_stock_refilled_stock_refilled_by'),
        ('supplyitems', '0006_supplyitems_created_supplyitems_last_edited_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SupplyItems',
            new_name='SupplyItem',
        ),
    ]
