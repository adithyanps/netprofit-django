# Generated by Django 2.2.4 on 2019-08-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_yearcharts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseYearChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=6)),
                ('grant_total', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]