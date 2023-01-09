from django.urls import path
from orders.views import create_order_status, list_orders_status, create_payment_method, list_payment_methods

urlpatterns = [
    path('create-order-status/', create_order_status),
    path('list-orders-status/', list_orders_status),
    path('create-payment-method/', create_payment_method),
    path('list-payment-methods/', list_payment_methods),
]
