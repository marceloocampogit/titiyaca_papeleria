from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=100)

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.IntegerField()
    category_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_description = models.CharField(max_length=200)