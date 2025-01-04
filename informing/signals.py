from django.db.models.signals import post_save
from django.dispatch import receiver

from common.utils.notification import NotificationService
from informing.models import Notification

SmsService = NotificationService(type_='sms')
EmailService = NotificationService(type_='email')
WebSocketService = NotificationService(type_='websocket')


@receiver(post_save, sender=Notification)
def send_notification(sender, instance: Notification, created, **kwargs):
    if created:
        if instance.type == instance.TypeChoices.WARNING:
            SmsService.send(to=instance.user.phone_number, message=instance.content)
        EmailService.send(to=instance.user.email, message=instance.content)
        WebSocketService.send(to=instance.user.id, message=instance.content)
