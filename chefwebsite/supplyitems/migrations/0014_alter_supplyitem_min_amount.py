# Generated by Django 5.0.1 on 2024-01-26 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplyitems', '0013_alter_supplyitem_max_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplyitem',
            name='min_amount',
            field=models.IntegerField(default=0, help_text="Below this amount, stock is 'low'"),
        ),
    ]