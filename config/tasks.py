from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.conf import settings
from django.core.mail import send_mail

from melipayamak import Api

SMS_USERNAME = settings.SMS_USERNAME
SMS_PASSWORD = settings.SMS_PASSWORD
SMS_FROM = settings.SMS_FROM
EMAIL_FROM = settings.EMAIL_HOST_USER

api = Api(SMS_USERNAME, SMS_PASSWORD)
sms = api.sms()


@shared_task
def send_sms(to, subject=None, message=None):
    subject = subject if subject else 'CoNote'
    message = message if message else 'Welcome to CoNote'
    text = f"{subject}: {message}"
    sms.send(to, SMS_FROM, text)


@shared_task
def send_email(to, subject=None, message=None):
    subject = subject if subject else 'CoNote'
    message = message if message else 'Welcome to CoNote'
    recipient_list = [to]
    send_mail(subject, message, EMAIL_FROM, recipient_list)


@shared_task
def send_websocket(to, subject=None, message=None):
    layer = get_channel_layer()
    data = {
        "type": f"send_notification",
        "message": "update",
        "content": message
    }
    async_to_sync(layer.group_send)(
        f"notification_{to}",
        data
    )
