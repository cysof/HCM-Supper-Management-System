from django.contrib import admin
from .models import CustomUser


class CustomerUserAdmin(admin.ModelAdmin):
    """
    CustomUser ModelAdmin with fields, list_display and list_filter
    for the admin interface.
    """
    fields = ['username','first_name', 'last_name', 'phone_number', 'email', 'dob', 'address']
    list_display = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'dob']
    list_filter = ['phone_number']


admin.site.register(CustomUser)
