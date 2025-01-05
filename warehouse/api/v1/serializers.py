from django.contrib.auth import get_user_model
from rest_framework import serializers

from common.fields import SignedURLImageField
from warehouse.models import Product, Invoice, Transaction

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    image = SignedURLImageField()

    class Meta:
        model = Product
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Invoice
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
