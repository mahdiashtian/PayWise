from datetime import timedelta

from .base import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
    }
}

# JWT Authentication
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=20),

    'AUTH_HEADER_TYPES': ('Bearer',),

    'JTI_CLAIM': 'jti',
}

DEV_APPS = ['drf_spectacular']
INSTALLED_APPS += DEV_APPS

SPECTACULAR_SETTINGS = {
    'TITLE': 'PayWise',
    'DESCRIPTION': 'A Simple Project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
