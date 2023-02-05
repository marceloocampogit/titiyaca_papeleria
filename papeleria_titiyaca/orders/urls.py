from django.urls import path
from orders.views import OrderCreateView, OrderUpdateView, OrderDeleteView, OrdersListView, \
     OrderItemsCreateView, OrderItemsUpdateView, update_order_item, delete_order_item, list_order_items, \
     update_order_status_reg_user, \
     OrderStatusCreateView,  OrderStatusListView, OrderStatusUpdateView, OrderStatusDeleteView, \
PaymentMethodCreateView, PaymentMethodUpdateView, PaymentMethodDeleteView, PaymentMethodListView

urlpatterns = [    
    # -- Order --------------------------------------------------------------------------------------
    path('create-order/', OrderCreateView.as_view() , name='create_order'),
    # --
    path('update-order/<int:pk>/', OrderUpdateView.as_view() , name='update_order'),
    # --
    path('update-order-status-reg-user/<int:pk>/', update_order_status_reg_user),    
    # --
    path('delete-order/<int:pk>/', OrderDeleteView.as_view() , name='delete_order'),
    # --
    path('list-orders/', OrdersListView.as_view(), name='list_orders'),
    # -- Order Items --------------------------------------------------------------------------------
    path('create-order-items/', OrderItemsCreateView.as_view() , name='create_order_items'),
    # --
    path('update-order-items/<int:pk>/', update_order_item),    
    # --
    path('delete-order-items/<int:pk>/', delete_order_item),
    # --
    path('list-order-items/<int:pk>/', list_order_items, name='list_orders_items'),
    # -- Order Status -------------------------------------------------------------------------------
    path('create-order-status/', OrderStatusCreateView.as_view() , name='create_order_status'),
    # --
    path('update-order-status/<int:pk>/', OrderStatusUpdateView.as_view() , name='update_order_status'),
    # --    
    path('delete-order-status/<int:pk>/', OrderStatusDeleteView.as_view() , name='delete_order_status'),
    # --    
    path('list-orders-status/', OrderStatusListView.as_view(), name='list_orders_status'),
    # -- Payment Method -------------------------------------------------------------------------------
    path('create-payment-method/', PaymentMethodCreateView.as_view() , name='create_payment_method'),
    # --    
    path('update-payment-method/<int:pk>/', PaymentMethodUpdateView.as_view() , name='update_payment_method'),
    # --
    path('delete-payment-method/<int:pk>/', PaymentMethodDeleteView.as_view() , name='delete_payment_method'),
    # --
    path('list-payment-methods/', PaymentMethodListView.as_view(), name='list_payment_methods'),
]
