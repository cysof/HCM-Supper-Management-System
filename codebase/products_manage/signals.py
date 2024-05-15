from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def update_stock_on_product_save(sender, instance, created, **kwargs):
    if created:
        instance.stock_quantity = instance.reorder_point
    instance.save()

@receiver(post_delete, sender=Product)
def update_stock_on_product_delete(sender, instance, **kwargs):
    instance.stock_quantity = instance.reorder_point
    instance.save()
    