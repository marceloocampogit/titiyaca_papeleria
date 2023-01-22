from django.db import models

# Create your models here.
class Categories(models.Model):
    category_code = models.IntegerField(unique= True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_code

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.IntegerField(unique= True)
    category_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.product_code