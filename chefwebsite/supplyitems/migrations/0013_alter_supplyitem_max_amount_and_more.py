# Generated by Django 5.0.1 on 2024-01-26 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplyitems', '0012_alter_supplyitem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplyitem',
            name='max_amount',
            field=models.IntegerField(default=0, help_text="At this amount, stock is at 'max recommended', above it is 'above max recommended'"),
        ),
        migrations.AlterField(
            model_name='supplyitem',
            name='med_amount',
            field=models.IntegerField(default=0, help_text="Below this amount, stock is at 'medium' amount"),
        ),
        migrations.AlterField(
            model_name='supplyitem',
            name='min_amount',
            field=models.IntegerField(default=0, verbose_name="Below this amount, stock is 'low'"),
        ),
    ]