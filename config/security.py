import jwt
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework_simplejwt.tokens import UntypedToken

User = get_user_model()


def set_jwt_access_cookie(response, access_token):
    """
    Set the JWT access token as a cookie in the response

    Args:
        response (HttpResponse): The response object
        access_token (str): The JWT access token

    Returns:
        None
    """

    cookie_name = getattr(settings, 'JWT_AUTH_COOKIE', None)
    access_token_expiration = (timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
    cookie_secure = getattr(settings, 'JWT_AUTH_SECURE', False)
    cookie_httponly = getattr(settings, 'JWT_AUTH_HTTPONLY', True)
    cookie_samesite = getattr(settings, 'JWT_AUTH_SAMESITE', 'Lax')

    if cookie_name:
        response.set_cookie(
            cookie_name,
            access_token,
            expires=access_token_expiration,
            secure=cookie_secure,
            httponly=cookie_httponly,
            samesite=cookie_samesite,
        )


def set_jwt_refresh_cookie(response, refresh_token):
    """
    Set the JWT refresh token as a cookie in the response

    Args:
        response (HttpResponse): The response object
        refresh_token (str): The JWT refresh token

    Returns:
        None
    """

    refresh_token_expiration = (timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
    refresh_cookie_name = getattr(settings, 'JWT_AUTH_REFRESH_COOKIE', None)
    refresh_cookie_path = getattr(settings, 'JWT_AUTH_REFRESH_COOKIE_PATH', '/')
    cookie_secure = getattr(settings, 'JWT_AUTH_SECURE', False)
    cookie_httponly = getattr(settings, 'JWT_AUTH_HTTPONLY', True)
    cookie_samesite = getattr(settings, 'JWT_AUTH_SAMESITE', 'Lax')

    if refresh_cookie_name:
        response.set_cookie(
            refresh_cookie_name,
            refresh_token,
            expires=refresh_token_expiration,
            secure=cookie_secure,
            httponly=cookie_httponly,
            samesite=cookie_samesite,
            path=refresh_cookie_path,
        )


def unset_jwt_cookies(response):
    """
    Unset the JWT cookies in the response

    Args:
        response (HttpResponse): The response object

    Returns:
        None
    """

    cookie_name = getattr(settings, 'JWT_AUTH_COOKIE', None)
    refresh_cookie_name = getattr(settings, 'JWT_AUTH_REFRESH_COOKIE', None)
    refresh_cookie_path = getattr(settings, 'JWT_AUTH_REFRESH_COOKIE_PATH', '/')
    cookie_samesite = getattr(settings, 'JWT_AUTH_SAMESITE', 'Lax')

    if cookie_name:
        response.delete_cookie(cookie_name, samesite=cookie_samesite)
    if refresh_cookie_name:
        response.delete_cookie(refresh_cookie_name, path=refresh_cookie_path, samesite=cookie_samesite)


def set_jwt_cookies(response, access_token, refresh_token):
    """
    Set the JWT cookies in the response

    Args:
        response (HttpResponse): The response object
        access_token (str): The JWT access token
        refresh_token (str): The JWT refresh token

    Returns:
        None
    """

    set_jwt_access_cookie(response, access_token)
    set_jwt_refresh_cookie(response, refresh_token)


class JWTAuthMiddleware(BaseMiddleware):
    @database_sync_to_async
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return AnonymousUser()

    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        token = None

        # Extract token from the headers
        if b'authorization' in headers:
            auth_header = headers[b'authorization'].decode().split()
            if len(auth_header) == 2 and auth_header[0].lower() == "bearer":
                token = auth_header[1]

        if token:
            try:
                UntypedToken(token)  # Validate token
                decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user_id = decoded_data.get('user_id')

                # Get user asynchronously
                scope['user'] = await self.get_user(user_id)
            except (ExpiredSignatureError, InvalidTokenError):
                scope['user'] = AnonymousUser()
        else:
            scope['user'] = AnonymousUser()

        return await super().__call__(scope, receive, send)