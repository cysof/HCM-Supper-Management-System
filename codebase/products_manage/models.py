from django.db import models

"""Model for products. this will house the list of all products in the app
"""


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    reorder_point = models.PositiveIntegerField(default=0)

    
    def __str__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: The name of the object.
        """
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
