# Generated by Django 2.2.4 on 2019-09-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_creditnotenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditnote',
            name='Doc_no',
            field=models.CharField(max_length=30),
        ),
    ]
