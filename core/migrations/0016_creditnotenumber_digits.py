# Generated by Django 2.2.4 on 2019-09-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20190919_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnotenumber',
            name='digits',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]