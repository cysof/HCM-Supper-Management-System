from django.contrib import admin
from .models import Product, CustomUser, Purches



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email']
    list_filter = ['phone_number']

class PurchesAdmin(admin.ModelAdmin):
    list_display = ['customer']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Purches, PurchesAdmin)
