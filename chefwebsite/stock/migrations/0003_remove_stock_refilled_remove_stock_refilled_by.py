# Generated by Django 5.0.1 on 2024-01-24 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_refilled_stock_refilled_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='refilled',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='refilled_by',
        ),
    ]
