import os

from django.utils.crypto import get_random_string


def random_string(length=18):
    return get_random_string(length)
