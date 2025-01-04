import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model

User = get_user_model()


class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        user = self.scope['user']
        if user.is_authenticated:
            self.group_name = f"notification_{user.id}"
            async_to_sync(self.channel_layer.group_add)(
                self.group_name, self.channel_name
            )
            self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass

    def send_notification(self, value):
        self.send(text_data=json.dumps(value, ensure_ascii=False))
