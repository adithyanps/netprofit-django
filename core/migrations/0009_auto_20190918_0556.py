# Generated by Django 2.2.4 on 2019-09-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190918_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesinvoicenu',
            name='child',
        ),
        migrations.AddField(
            model_name='salesinvoicenu',
            name='child',
            field=models.ManyToManyField(to='core.InvoiceLine'),
        ),
    ]