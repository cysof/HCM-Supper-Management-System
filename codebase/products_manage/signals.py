from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def update_stock_on_product_save(sender, instance, created, **kwargs):
    """
    A function that updates the stock of a product when a new product is saved.

    Parameters:
        sender: The sender of the signal.
        instance: The product instance being saved.
        created: A boolean indicating if the product is being created.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if created:
        instance.stock += instance.stock_quantity  # Update stock based on stock quantity
        instance.save()

@receiver(post_delete, sender=Product)
def update_stock_on_product_delete(sender, instance, **kwargs):
    """
    A function that updates the stock of a product when the product is deleted.

    Parameters:
        sender: The sender of the signal.
        instance: The product instance being deleted.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    product_stock = instance.stock_quantity  # Retrieve stock quantity before deletion
    instance.stock -= product_stock  # Subtract stock quantity from the stock
    instance.save()
