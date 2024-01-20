# Generated by Django 5.0.1 on 2024-01-20 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplyitems', '0002_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('item_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplyitems.supplyitems')),
            ],
        ),
    ]