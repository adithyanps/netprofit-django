# Generated by Django 2.2.4 on 2019-09-22 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Masters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('transaction_type', models.CharField(blank=True, choices=[('SALES', 'Sales'), ('PURCHASE', 'Purchase'), ('DEBITNOTE', 'DebitNote'), ('CREDITNOTE', 'CreditNote'), ('COSTOMER_RECIEPT', 'CustomerReceipt'), ('SUPPLIER_PAYMENT', 'SupplierPayment'), ('EXPENSE', 'Expense'), ('JOURNAL', 'Journal')], default='SALES', max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JournalItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('credit_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Masters.Account')),
                ('journal_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Journal_Entry.JournalEntry')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Masters.Partner')),
            ],
        ),
    ]