import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
import json

# Create your models here.
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=60,null=False)


class Expenses(models.Model):
    Doc_no = models.CharField(max_length=60,null=False)
    ExpenseCategory = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, null=False, blank=False)
    Date = models.DateField()
    ExpenseAcct = models.ForeignKey('Masters.Account', on_delete=models.CASCADE, null=False, blank=False)
    CreditAcct = models.ForeignKey('Masters.Account',related_name='CreditAcct', on_delete=models.CASCADE, null=False, blank=False)
    Amount = models.DecimalField(max_digits=15,decimal_places=2)
    journal_entry = models.ForeignKey('Journal_Entry.JournalEntry', on_delete=models.CASCADE, null=True, blank=True)
