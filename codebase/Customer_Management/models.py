from django.contrib.auth.models import AbstractUser
from django.db import models
from products_manage.models import Price,Product

class CustomUser(AbstractUser):
    # Your custom fields and methods here
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()
    dob = models.DateField()
    address = models.CharField(max_length=150)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
    )


class Purches(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,related_name='purches')
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

"""
next model to be created. that will take care of the activity
of a customer. it will have relationship with customer models
#Purchase history
#Preferences and interests

"""



