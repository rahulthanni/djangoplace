# Generated by Django 4.0.6 on 2022-07-28 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishesapi', '0002_rename_dish_dishes_dishes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dishes',
            old_name='dishes',
            new_name='dish_name',
        ),
    ]
