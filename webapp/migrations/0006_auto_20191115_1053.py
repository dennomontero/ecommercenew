# Generated by Django 2.2.6 on 2019-11-15 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20191114_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items',
            new_name='item',
        ),
    ]
