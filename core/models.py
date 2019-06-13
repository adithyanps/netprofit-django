import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
import json


# auth models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """create and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError("users must have a password")

        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        """creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    CHOICES = (
        ('FULL_ACCESS', 'Full_access'),
        ('ACCOUNTANT', 'Accountant'),
        ('READ_ONLY', 'Read_only'),
    )
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    user_choice = models.CharField(max_length=15, choices=CHOICES, default='FULL_ACCESS',)


    objects = UserManager()
    USERNAME_FIELD = 'email'

#invoice models

class Customer(models.Model):
    customer = models.CharField(max_length=50)
    def __str__(self):
        return self.customer


class Branch(models.Model):
    branch = models.CharField(max_length=50)
    def __str__(self):
        return self.branch

class Item(models.Model):
    item = models.CharField(max_length=50,null=False)
    price = models.DecimalField(max_digits=15,decimal_places=2)

    def __str__(self):
        return self.item

# Journal entry


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


class Account(models.Model):
    CHOICES = (
        ('RECIEVABLE', 'Receivable'),
        ('PAYABLE', 'Payable'),
        ('SALES', 'Sales'),
        ('PURCHASE', 'Purchase'),
        ('EXPENSE', 'Expense'),
        ('INCOME', 'Income'),
        ('CASH', 'Cash'),
        ('BANK', 'Bank'),
    )

    type = models.CharField(max_length=15, choices=CHOICES, default='RECIEVABLE',)
    name = models.CharField(max_length=150)


class AccountDefault(models.Model):
    SalesAccont = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='SalesAcnt',null=True, blank=True)
    PurchaseAccont = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='PurchaseAcnt',null=True, blank=True)
    CustomerAccount = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='CustomerAcnt',null=True, blank=True)
    SupplierAccount = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='SupplierAcnt',null=True, blank=True)

class JournalItem(models.Model):
    journal_entry = models.ForeignKey('core.JournalEntry', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    partner = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    debit_amount = models.DecimalField(max_digits=15,decimal_places=2,null=True, blank=True)
    credit_amount = models.DecimalField(max_digits=15,decimal_places=2,null=True, blank=True)
#


class Parent(models.Model):
    invoice_no = models.IntegerField()
    doc_no = models.IntegerField(null=True,blank=True)
    customer = models.CharField(max_length=50,null=False,blank=True)
    branch = models.CharField(max_length=50,null=False)
    status = models.BooleanField(default=False, null=True,blank=True)
    narration = models.CharField(max_length=500, null=True,blank=True)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=15,decimal_places=2)
    discount = models.DecimalField(max_digits=15,decimal_places=2, null=True,blank=True)
    grant_total = models.DecimalField(max_digits=15,decimal_places=2)
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title
    #
    @property
    def child(self):
        return self.childinvoice_set.all()


class ChildInvoice(models.Model):
    key = models.ForeignKey('core.Parent', on_delete=models.CASCADE)
    item = models.CharField(max_length=60,null=False)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    sub_total = models.DecimalField(max_digits=15,decimal_places=2)

class InvoiceLine(models.Model):
    item = models.CharField(max_length=60,null=False)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    sub_total = models.DecimalField(max_digits=15,decimal_places=2)

class SalesInvoice(models.Model):
    invoice_no = models.IntegerField()
    doc_no = models.IntegerField(null=True,blank=True)
    customer = models.CharField(max_length=50,null=False,blank=True)
    branch = models.CharField(max_length=50,null=False)
    status = models.BooleanField(default=False, null=True,blank=True)
    narration = models.CharField(max_length=500, null=True,blank=True)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=15,decimal_places=2)
    discount = models.DecimalField(max_digits=15,decimal_places=2, null=True,blank=True)
    grant_total = models.DecimalField(max_digits=15,decimal_places=2)
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, null=True, blank=True)
    child = models.ManyToManyField(InvoiceLine)

class CustomerReceipt(models.Model):
    reciept_no = models.IntegerField()
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, null=True, blank=True)


# expense
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=60,null=False)

class Expenses(models.Model):
    Doc_no = models.IntegerField()
    ExpenseCategory = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, null=False, blank=False)
    Date = models.DateField()
    ExpenseAcct = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    CreditAcct = models.ForeignKey(Account,related_name='CreditAcct', on_delete=models.CASCADE, null=False, blank=False)
    Amount = models.DecimalField(max_digits=15,decimal_places=2)
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, null=True, blank=True)
