from django.db import models
from categories.models import Category
from products.models   import Product

# Create your models here.
class Drop(models.Model):
    timer = models.TimeField()
    time = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
