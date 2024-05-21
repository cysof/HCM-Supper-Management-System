from django.db import models
from accounts.models import CustomUser

"""Model for products. this will house the list of all products in the app
"""

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


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=150, blank=True)
   

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    reorder_point = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def update_stock(self, quantity):
        """
        Update the stock quantity of the product by the given quantity.

        Parameters:
            quantity (int): The quantity to update the stock quantity by.

        Returns:
            None
        """
        self.stock_quantity += quantity
        self.save()

    def get_product_quantity(self):
        """
        Get the current stock quantity of the product.

        Returns:
            int: The current stock quantity of the product.
        """
        return self.stock_quantity
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order: {self.order.id})"



