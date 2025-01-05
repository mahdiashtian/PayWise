from django.urls import path, include
from rest_framework.routers import DefaultRouter

from warehouse.api.v1.api_views import ProductViewSet, InvoiceViewSet, TransactionViewSet

app_name = 'warehouse'

routers = DefaultRouter()
routers.register(r'products', ProductViewSet, basename='products')
routers.register(r'invoices', InvoiceViewSet, basename='invoices')
routers.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path("v1/", include(routers.urls)),
]
