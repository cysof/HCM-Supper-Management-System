from django.core.mail import send_mail

def send_reorder_alert(product):
    subject = f"Reorder Alert: {product.name}"
    message = f"The stock of {product.name} is below the reorder point."
    recipient_list = ["cp4reallife@gmail.com"]  # Replace with the actual recipient email address
    send_mail(subject, message, recipient_list)