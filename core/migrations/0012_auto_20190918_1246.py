# Generated by Django 2.2.4 on 2019-09-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190918_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceline',
            name='item',
            field=models.CharField(max_length=60),
        ),
    ]
