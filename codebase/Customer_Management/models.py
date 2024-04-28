from django.db import models
from products_manage .models import Product, Price

"""Customer_Management this model manage customer information and their
order in the portal.
"""

class CustomerBio(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()
    dob = models.DateField()
    address = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.first_name


class Purches(models.Model):
    customer = models.ForeignKey(CustomerBio, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,related_name='purches')
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

"""
next model to be created. that will take care of the activity
of a customer. it will have relationship with customer models
#Purchase history
#Preferences and interests

"""



