# Generated by Django 2.2.4 on 2019-09-23 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Masters', '0001_initial'),
        ('Journal_Entry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doc_no', models.IntegerField()),
                ('Date', models.DateField()),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('CreditAcct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CreditAcct', to='Masters.Account')),
                ('ExpenseAcct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Masters.Account')),
                ('ExpenseCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Expenses.ExpenseCategory')),
                ('journal_entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Journal_Entry.JournalEntry')),
            ],
        ),
    ]
