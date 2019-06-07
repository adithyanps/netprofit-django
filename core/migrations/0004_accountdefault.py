# Generated by Django 2.1.3 on 2019-05-15 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190515_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDefault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerAccount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acct', to='core.Account')),
                ('PurchaseAccont', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acnt', to='core.Account')),
                ('SalesAccont', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accnt', to='core.Account')),
                ('SupplierAccount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accn', to='core.Account')),
            ],
        ),
    ]