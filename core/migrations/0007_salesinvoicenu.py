# Generated by Django 2.2.4 on 2019-09-18 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_invoiceline'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoiceNu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.IntegerField()),
                ('doc_no', models.IntegerField(blank=True, null=True)),
                ('customer', models.CharField(blank=True, max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('narration', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('grant_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('child', models.ManyToManyField(to='core.InvoiceLine')),
                ('journal_entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.JournalEntry')),
            ],
        ),
    ]