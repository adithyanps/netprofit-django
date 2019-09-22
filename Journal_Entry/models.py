import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
import json

class JournalEntry(models.Model):
    CHOICES = (
        ('SALES', 'Sales'),
        ('PURCHASE', 'Purchase'),
        ('DEBITNOTE', 'DebitNote'),
        ('CREDITNOTE', 'CreditNote'),
        ('COSTOMER_RECIEPT', 'CustomerReceipt'),
        ('SUPPLIER_PAYMENT', 'SupplierPayment'),
        ('EXPENSE', 'Expense'),
        ('JOURNAL', 'Journal'),
    )

    date = models.DateField()
    transaction_type = models.CharField(max_length=100, choices=CHOICES, default='SALES',null=True, blank=True)
    description = models.CharField(max_length=15,null=True, blank=True)

    @property
    def journal_item(self):
        return self.journalitem_set.all()

class JournalItem(models.Model):
    journal_entry = models.ForeignKey('Journal_Entry.JournalEntry', on_delete=models.CASCADE)
    account = models.ForeignKey('Masters.Account', on_delete=models.CASCADE, null=True, blank=True)
    partner = models.ForeignKey('Masters.Partner', on_delete=models.CASCADE, null=True, blank=True)
    debit_amount = models.DecimalField(max_digits=15,decimal_places=2,null=True, blank=True)
    credit_amount = models.DecimalField(max_digits=15,decimal_places=2,null=True, blank=True)
