# Generated by Django 2.2.4 on 2019-09-16 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190916_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
    ]
