from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

from django.utils.translation import gettext as _


# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields':('email','password') }),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields':('is_active','is_staff','is_superuser', 'user_choice')}),
        (_('Important dates'), {'fields':('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email' ,'password1', 'password2')
        }),
    )
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Customer)
admin.site.register(models.Branch)
admin.site.register(models.Item)
admin.site.register(models.AccountDefault)
