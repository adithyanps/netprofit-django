# Generated by Django 2.1.3 on 2019-05-09 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childinvoice',
            name='text',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='title',
        ),
    ]
