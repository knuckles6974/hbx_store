from django.db import models
from users.models  import User

# Create your models here.

class Support(models.Model):
    qna = models.TextField()
    returns = models.TextField()
    request = models.TextField()
    payment = models.CharField(max_length=30)
    orderstate = models.CharField(max_length=4000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
