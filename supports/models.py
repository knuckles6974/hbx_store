from django.db import models
from users.models  import User

# Create your models here.

class Support(models.Model):
    qna = models.TextField()
    returns = models.TextField()
    request = models.TextField()
    paymaent = models.CharField()
    orderstate = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
