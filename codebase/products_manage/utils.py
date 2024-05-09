from django.core.mail import send_mail

def send_reorder_alert(product):
    subject = f"Reorder Alert: {product.name}"
    message = f"The stock of {product.name} is below the reorder point."
    recipient_list = ["cp4reallife@gmail.com"]  # Replace with the actual recipient email address
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