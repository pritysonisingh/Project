# Generated by Django 2.2.2 on 2020-07-15 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]