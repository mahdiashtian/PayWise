from django.urls import path, include
from rest_framework.routers import DefaultRouter

from informing.api.v1.api_views import NotificationViewSet

app_name = 'informing'

routers = DefaultRouter()
routers.register(r'notification', NotificationViewSet, basename='notification')

urlpatterns = [
    path("v1/", include(routers.urls)),
]
