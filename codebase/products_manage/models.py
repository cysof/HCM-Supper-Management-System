from django.db import models

"""Model for products. this will house the list of all products in the app
"""

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default=0)
    reorder_point = models.PositiveIntegerField(default=5)

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

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
