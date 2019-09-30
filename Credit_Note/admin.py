from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from Credit_Note import models

# Register your models here.
admin.site.register(models.CreditNote)
