import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
import json

# Create your models here.
class Area(models.Model):
    area = models.CharField(max_length=50)

    def __str__(self):
        return self.area


class Partner(models.Model):
    CHOICES =(
    ('CUSTOMER','Customer'),
    ('SUPPLIER','Supplier'),
    ('BOTH','Both')
    )
    customer_id = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=100, choices=CHOICES, default='CUSTOMER',null=True, blank=True)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="created_bys",on_delete=models.CASCADE)
    edited_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="edited_bys",on_delete=models.CASCADE,null=True,blank=True)

    # class Meta:
    #     abstract = True
class ProductCategory(models.Model):
    name = models.CharField(max_length=50,null=False)
    ParentCategory = models.ForeignKey('Masters.ProductCategory',on_delete=models.CASCADE, null=True,blank=True)


class Product(models.Model):
    item = models.CharField(max_length=50,null=False)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    product_Cat = models.ForeignKey('Masters.ProductCategory',on_delete=models.CASCADE)

    def __str__(self):
        return self.item

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

class Branch(models.Model):
    branch = models.CharField(max_length=50)
    def __str__(self):
        return self.branch
