from django.db import models
from products.models import Products

# Create your models here.

class OrderStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class PaymentMethod(models.Model):
    payment_method_large = models.CharField(max_length=20)
    payment_method_short = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_code = models.IntegerField()    
    order_price = models.FloatField()
    creation_time = models.DateTimeField(auto_now_add=True)    
    payment_method_short = models.ForeignKey(PaymentMethod, on_delete= models.CASCADE)     
    status = models.ForeignKey(OrderStatus, on_delete= models.CASCADE)
    client_name = models.CharField(max_length=100, blank= True)

    def __str__(self):
        return self.name

class OrderItems(models.Model):
    order_code = models.ForeignKey(Orders, on_delete= models.CASCADE)     
    item_code = models.IntegerField()
    product_code = models.ForeignKey(Products, on_delete= models.CASCADE)

    def __str__(self):
        return self.name