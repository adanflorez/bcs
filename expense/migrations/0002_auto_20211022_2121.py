# Generated by Django 3.2.8 on 2021-10-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='category',
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ManyToManyField(to='category.Category'),
        ),
    ]
