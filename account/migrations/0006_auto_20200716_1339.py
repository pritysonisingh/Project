# Generated by Django 2.2.2 on 2020-07-16 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200716_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='user',
            new_name='users',
        ),
    ]
