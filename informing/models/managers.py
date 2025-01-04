from django.db import models
from django.db.models.manager import BaseManager


class NotificationQuerySet(models.QuerySet):
    def error(self):
        return self.filter(type="error")

    def warning(self):
        return self.filter(type="warning")

    def info(self):
        return self.filter(type="info")


class NotificationManager(BaseManager):
    def get_queryset(self):
        return NotificationQuerySet(self.model, using=self._db)

    def error(self):
        return self.get_queryset().error()

    def warning(self):
        return self.get_queryset().warning()

    def info(self):
        return self.get_queryset().info()
