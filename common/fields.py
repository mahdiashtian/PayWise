from django.core.cache import cache
from rest_framework import serializers

from common.utils.file_func import generate_signed_url


class BaseSignedField:
    @staticmethod
    def to_representation(value):
        if value and hasattr(value, 'name'):
            print(value.name)
            print(value)
            cache_key = f"signed_url_{value.name}"
            signed_url = cache.get(cache_key)

            if not signed_url:
                signed_url = generate_signed_url(value.name)
                cache.set(cache_key, signed_url, timeout=300)
            return signed_url
        return None


class SignedURLFileField(BaseSignedField, serializers.FileField):
    ...


class SignedURLImageField(BaseSignedField, serializers.ImageField):
    ...
