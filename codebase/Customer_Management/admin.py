from django.contrib import admin
from .models import Product, CustomerBio, Purches



class CustomerBioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email']
    list_filter = ['phone_number']

class PurchesAdmin(admin.ModelAdmin):
    list_display = ['customer']


admin.site.register(CustomerBio, CustomerBioAdmin)
admin.site.register(Purches, PurchesAdmin)
