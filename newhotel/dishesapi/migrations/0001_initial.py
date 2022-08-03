# Generated by Django 4.0.6 on 2022-07-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]