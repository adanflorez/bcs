# Generated by Django 3.2.8 on 2021-10-23 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20211023_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='start_date',
        ),
    ]
