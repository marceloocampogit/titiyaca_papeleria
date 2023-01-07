from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete= models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=200)