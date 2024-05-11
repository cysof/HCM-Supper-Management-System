from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Product

@receiver(post_save, sender=Product)
def check_stock_levels(sender, instance, created, **kwargs):
    if instance.stock_quantity < instance.reorder_point:
        subject = f"Alert: Stock level below reorder point for product {instance.name}"
        message = f"The stock level for product {instance.name} is below the reorder point. Current stock level: {instance.stock_quantity}"
        send_mail(subject, message, 'cp4reallife@gmail.com', ['cp4reallife@yahoo.com'])