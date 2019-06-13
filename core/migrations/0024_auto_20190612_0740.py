# Generated by Django 2.1.3 on 2019-06-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190612_0733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesinvoice',
            name='invoice_line',
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='invoice_line',
            field=models.ManyToManyField(to='core.InvoiceLine'),
        ),
    ]
