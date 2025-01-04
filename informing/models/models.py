from django.db import models

from informing.models.managers import NotificationManager


class Notification(models.Model):
    class TypeChoices(models.TextChoices):
        INFO = 'info'
        WARNING = 'warning'
        ERROR = 'error'

    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    type = models.CharField(max_length=10, choices=TypeChoices.choices, default=TypeChoices.INFO)
    objects = NotificationManager()

    def __str__(self):
        return self.title

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.content = f"{self.type} : {self.content}"
        super().save(force_insert, force_update, using, update_fields)
