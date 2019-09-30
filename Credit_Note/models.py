import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
import json


class CreditNote(models.Model):
    Doc_no = models.CharField(max_length=30, null=False,blank=False)
    Partner = models.ForeignKey('Masters.Partner',on_delete=models.CASCADE, null=True, blank=True)
    Grand_total = models.DecimalField(max_digits=15,decimal_places=2)
    Date = models.DateField()
    Comment = models.CharField(max_length=500, null=True,blank=True)
    journal_entry = models.ForeignKey('Journal_Entry.JournalEntry', on_delete=models.CASCADE, null=True, blank=True)
