from django.contrib.auth import get_user_model
from rest_framework import serializers

from informing.models import Notification

User = get_user_model()


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
