from django.template import Context
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage

def send_contact_email():
    context = {
        'full_name': 'Ritvik Dayal',
        'email': 'ritvikd9@gmail.com',
        'phone_number': '9457614680',
        'message': 'Hello from the other side!!',
    }

    email_subject = 'Contact Message | Portfolio'

    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, ['ritvikr1605@gmail.com', ],
    )

    return email.send(fail_silently=False)