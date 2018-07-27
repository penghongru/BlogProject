from django.contrib import admin

# Register your models here.
from login import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sex', 'create_time']


admin.site.register(models.User, UserAdmin)
