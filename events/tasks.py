
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_event_email(event_title, recipient_email):
    send_mail(
        'New Event Notification',
        f'The event "{event_title}" has been created.',
        'from@example.com',
        [recipient_email],
    )
