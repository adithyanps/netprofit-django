# Generated by Django 2.2.4 on 2019-09-20 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20190919_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnote',
            name='journal_entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.JournalEntry'),
        ),
    ]
