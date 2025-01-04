from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from informing.consumers import NotificationConsumer
from config.security import JWTAuthMiddleware
from django.core.asgi import get_asgi_application

websocket_urlpatterns = [
    path("ws/notification/", NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JWTAuthMiddleware(
        URLRouter(websocket_urlpatterns)
    ),
})