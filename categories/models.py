from django.db import models

# Create your models here.
class Category(models.Model):
    men = models.CharField(max_length=50)
    woman = models.CharField(max_length=50)
    life = models.CharField(max_length=50)
    sale = models.CharField(max_length=50)
