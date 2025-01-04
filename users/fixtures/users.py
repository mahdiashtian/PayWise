import random

from users.models import *
from model_bakery.baker import make


def create_sample_users(_quantity=10):
    make(User, _quantity=_quantity)
    print("Sample users created successfully.")
