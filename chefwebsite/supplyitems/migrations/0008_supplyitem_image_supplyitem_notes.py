# Generated by Django 5.0.1 on 2024-01-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplyitems', '0007_rename_supplyitems_supplyitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplyitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='supplyitem',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
