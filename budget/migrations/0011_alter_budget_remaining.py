# Generated by Django 3.2.8 on 2021-10-26 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0010_alter_budget_remaining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='remaining',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
