from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from config.permissions import IsSuperUserOrReadOnly
from warehouse.api.v1.serializers import ProductSerializer, InvoiceSerializer, TransactionSerializer
from warehouse.models import Product, Invoice, Transaction


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().prefetch_related('invoices')
    serializer_class = ProductSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class InvoiceViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    ordering_fields = ['id']

    def get_queryset(self):
        user = self.request.user
        queryset = Invoice.objects.select_related('user').prefetch_related('products')
        if user.is_superuser:
            return queryset
        return queryset.filter(user=user)


class TransactionViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['invoice', 'status']
    ordering_fields = ['id']

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.select_related('invoice__user')
        if user.is_superuser:
            return queryset
        return queryset.filter(invoice__user=user)
