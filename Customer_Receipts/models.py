import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
import json


# Create your models here.
class CustomerReceipt(models.Model):
    reciept_no = models.CharField(max_length=60,null=False)
    journal_entry = models.ForeignKey('Journal_Entry.JournalEntry', on_delete=models.CASCADE, null=True, blank=True)
