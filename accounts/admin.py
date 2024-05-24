from django.contrib import admin
from .models import CustomUser




class CustomAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_active']


admin.site.register(CustomUser, CustomAdmin)