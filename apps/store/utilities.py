from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from apps.order.views import render_to_pdf


def decrement_product_quantity(order):
    for item in order.items.all():
        product = item.product
        product.num_available = product.num_available - item.quantity
        product.save()


def send_order_confirmation(order):
    subject = 'Order confirmation'
    from_email = 'noreply@phucanhgears.com'
    to = ['mail@phucanhgear.com', order.email]
    text_content = 'Your order has been sent!'
    html_content = render_to_string('order_confirmation.html', {'order': order})

    pdf = render_to_pdf('order_pdf.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")

    if pdf:
        name = 'order_%s.pdf' % order.id
        msg.attach(name, pdf, 'application/pdf')

    msg.send()