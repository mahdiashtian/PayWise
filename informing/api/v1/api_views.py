from rest_framework.viewsets import ModelViewSet

from config.permissions import IsSuperUser
from informing.api.v1.serializers import NotificationSerializer
from informing.models import Notification


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsSuperUser]
