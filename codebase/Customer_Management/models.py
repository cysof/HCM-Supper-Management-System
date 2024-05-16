from django.contrib.auth.models import AbstractUser
from django.db import models
from products_manage.models import Price,Product

ORDER_STATUS = (
    ('Pending', 'Pending'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
    ('Returned', 'Returned'),
    ('Refunded', 'Refunded'),
    ('Failed', 'Failed'),
    ('Completed', 'Completed'),
    ('Processing', 'Processing'),
)

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

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order.user.username} - {self.product.name}"
    

"""
next model to be created. that will take care of the activity
of a customer. it will have relationship with customer models
#Purchase history
#Preferences and interests

"""



