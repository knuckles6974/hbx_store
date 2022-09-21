from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=7)
    sizeguide = models.CharField(max_length=2000)
    description = models.TextField()
    quantity = models.IntegerField()
    interestproduct = models.BooleanField()
    
    
    class Meta:
        db_table = 'products'