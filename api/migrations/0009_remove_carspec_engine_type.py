# Generated by Django 4.2.2 on 2024-01-08 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_carspec_car_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carspec',
            name='engine_type',
        ),
    ]