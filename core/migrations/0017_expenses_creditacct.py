# Generated by Django 2.1.3 on 2019-06-07 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='CreditAcct',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='CreditAcct', to='core.Account'),
            preserve_default=False,
        ),
    ]
