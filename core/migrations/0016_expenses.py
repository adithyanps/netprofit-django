# Generated by Django 2.1.3 on 2019-06-07 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_expensecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doc_no', models.IntegerField()),
                ('Date', models.DateField()),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ExpenseAcct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Account')),
                ('ExpenseCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ExpenseCategory')),
            ],
        ),
    ]