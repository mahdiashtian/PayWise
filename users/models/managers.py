from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserQuerySet(models.QuerySet):
    def staff(self):
        return self.filter(is_staff=True)

    def superuser(self):
        return self.filter(is_superuser=True)


class UserManager(BaseUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def staff(self):
        return self.get_queryset().staff()

    def superuser(self):
        return self.get_queryset().superuser()
