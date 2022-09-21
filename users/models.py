from django.db   import models
from products.models  import Product


class User(models.Model):
    first_name = models.CharField(max_length=2, blank=False)
    last_name = models.CharField(max_length=2, blank=False)
    nickname = models.CharField(max_length=10, blank=False)
    profile_image_url = models.CharField(max_length=2000)
    email = models.EmailField(unique=True)
    password = models.IntegerField()
    phone_number = models.CharField(max_length=14)
    gender = models.BooleanField()
    
    
    class Meta:
        db_table = 'users'


class WishList(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = 'wishlists'