from django.db   import models
from django.contrib.auth.models  import AbstractUser
from products.models  import Product


class User(AbstractUser):
    
    username = models.CharField(max_length=30,null=True,unique=True)
    nickname = models.CharField(max_length=10, blank=False,null=True)
    profile_image_url = models.CharField(max_length=2000,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=30,null=True)
    phone_number = models.CharField(max_length=14,null=True)
    gender = models.BooleanField(null=True)
    


class WishList(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)