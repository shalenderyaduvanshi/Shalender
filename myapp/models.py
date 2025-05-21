from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.BigIntegerField()

    def __str__(self):
        return self.product_name