# Generated by Django 3.1.2 on 2020-12-11 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_drinks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
    ]
