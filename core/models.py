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

class P_Invoice(models.Model):
     """common elements of user data save here"""
     invoice_no = models.IntegerField()
     doc_no = models.IntegerField()
     customer = models.CharField(max_length=50,null=False)
     branch = models.CharField(max_length=50,null=False)
     status = models.BooleanField(default=False)
     narration = models.CharField(max_length=500)
     date = models.DateField()
     total_amount = models.DecimalField(max_digits=15,decimal_places=2)
     discount = models.DecimalField(max_digits=15,decimal_places=2)
     grant_total = models.DecimalField(max_digits=15,decimal_places=2)

class C_Invoice(models.Model):
    key = models.ForeignKey(P_Invoice, on_delete=models.CASCADE, related_name='child', null=True, blank=True)
    item = models.CharField(max_length=60,null=False)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    sub_total = models.DecimalField(max_digits=15,decimal_places=2)

    # def __str__(self):
    #     return self.item
