# Generated by Django 2.1.3 on 2019-06-07 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_expenses_creditacct'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='journal_entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.JournalEntry'),
        ),
    ]