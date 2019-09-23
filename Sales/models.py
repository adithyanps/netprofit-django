import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
import json


# Create your models here.

class InvoiceLine(models.Model):
    item = models.CharField(max_length=60,null=False)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    sub_total = models.DecimalField(max_digits=15,decimal_places=2)

class SalesInvoice(models.Model):
    invoice_no = models.IntegerField()
    doc_no = models.IntegerField(null=True,blank=True)
    customer = models.ForeignKey('Masters.Partner',on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey('Masters.Branch',on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False, null=True,blank=True)
    narration = models.CharField(max_length=500, null=True,blank=True)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=15,decimal_places=2)
    discount = models.DecimalField(max_digits=15,decimal_places=2, null=True,blank=True)
    grant_total = models.DecimalField(max_digits=15,decimal_places=2)
    journal_entry = models.ForeignKey('Journal_Entry.JournalEntry', on_delete=models.CASCADE, null=True, blank=True)
    child = models.ManyToManyField(InvoiceLine)
