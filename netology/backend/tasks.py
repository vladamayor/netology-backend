from django.core.mail import EmailMultiAlternatives

from netology.celery import application as celery


@celery.task
def send_email(subject, body, from_email, to):
    print(f"Send email to {to}")
    email = EmailMultiAlternatives(subject, body, from_email, to)
    email.send()
