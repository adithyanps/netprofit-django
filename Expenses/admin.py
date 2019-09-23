from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Expenses import models
from django.utils.translation import gettext as _


# Register your models here.

admin.site.register(models.ExpenseCategory)
