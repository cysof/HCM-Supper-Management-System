from django.db import models

"""Model for products. this will house the list of all products in the app
"""
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    stock_quantity = models.PositiveIntegerField(default=0)
    reorder_point = models.PositiveIntegerField(default=5)

    
    def __str__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: The name of the object.
        """
        return self.name
    
    def update_stock(self, quantity):
        """
        Update the stock of the product by the given quantity.

        Parameters:
            quantity (int): The quantity to update the stock by.

        Returns:
            None
        """
        self.stock += quantity
        self.save()

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
