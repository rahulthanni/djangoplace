# Generated by Django 4.0.6 on 2022-07-26 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='name',
            new_name='product_name',
        ),
    ]
