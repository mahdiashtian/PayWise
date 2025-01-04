from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView

from users.api.v1.api_views import UserViewSet, TokenUnsetView, TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenBlacklistView

app_name = 'user'

routers = DefaultRouter()
routers.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    re_path(r"^v1/auth/jwt/create/?", TokenObtainPairView.as_view(), name="jwt-create-v1"),
    re_path(r"^v1/auth/jwt/refresh/?", TokenRefreshView.as_view(), name="jwt-refresh-v1"),
    re_path(r"^v1/auth/jwt/verify/?", TokenVerifyView.as_view(), name="jwt-verify-v1"),
    re_path(r"^v1/auth/jwt/logout/?", TokenUnsetView.as_view(), name="jwt-logout-v1"),
    re_path(r"^v1/auth/jwt/blacklist/?", TokenBlacklistView.as_view(), name='jwt-blacklist-v1'),

    path("v1/", include(routers.urls)),
]
