# Generated by Django 2.1.3 on 2019-06-28 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childinvoice',
            name='key',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='journal_entry',
        ),
        migrations.DeleteModel(
            name='ChildInvoice',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
    ]
