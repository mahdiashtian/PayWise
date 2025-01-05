from datetime import timedelta

from .base import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# JWT Authentication
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=100),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=500),

    'AUTH_HEADER_TYPES': ('Bearer',),
    'JTI_CLAIM': 'jti',
}

LOCAL_APPS = ['drf_spectacular']
INSTALLED_APPS += LOCAL_APPS

SPECTACULAR_SETTINGS = {
    'TITLE': 'PayWise',
    'DESCRIPTION': 'A Simple Project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
