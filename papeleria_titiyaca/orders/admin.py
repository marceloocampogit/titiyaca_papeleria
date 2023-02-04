from django.contrib import admin

from orders.models import Orders, OrderStatus, PaymentMethod

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'order_price', 'creation_time', 'payment_method_short', 'status')

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['status']

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['payment_method_large']    