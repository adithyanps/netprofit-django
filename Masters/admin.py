from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from Masters import models

# Register your models here.
admin.site.register(models.Branch)
admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
admin.site.register(models.AccountDefault)
admin.site.register(models.Account)
admin.site.register(models.Partner)
admin.site.register(models.Area)
