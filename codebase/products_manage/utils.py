from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from .models import Product
from django.http import HttpResponse


def check_low_product(product_id, quantity_threshold):
    # Get the product instance
    product = get_object_or_404(Product, id=product_id)

    # Get the product quantity
    product_quantity = product.get_product_quantity()  # Assuming you have implemented this method in the Product model

    # Check if the quantity is below the threshold
    if product_quantity < quantity_threshold:
        # Send an email
        subject = 'Low Product Quantity'
        message = f'The quantity of product {product_id} is below the threshold.'
        from_email = 'cp4reallife@gmail.com'
        to_email = ['cp4reallife@yahoo.com']
        send_mail(subject, message, from_email, to_email)

        return True
    else:
        return False



def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email.'
    from_email = 'cp4reallife@gmail.com'
    to_email = ['cp4reallife@yahoo.com']
    send_mail(subject, message, from_email, to_email)
    return HttpResponse('Test email sent.')




def send_reorder_alert(product):
    subject = f"Reorder Alert: {product.name}"
    message = f"The stock of {product.name} is below the reorder point."
    recipient_list = ["cp4reallife@outlook.com"]  # Replace with the actual recipient email address
    send_mail(subject, message, recipient_list)

#def update_product_stock(product_id, quantity):
 #   try:
  #      product = Product.objects.select_for_update().get(pk=product_id)
   # except ObjectDoesNotExist:
    #    raise ValueError("Product not found")

    #product.stock += quantity
    #product.save()

    #if product.stock < product.reorder_point:
     #   send_reorder_alert(product)