
from .models   import User, WishList
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField 


class UserSerializer(ModelSerializer):
    
    
    
    
    class Meta:
        model = User
        fields = '__all__'
      
    
    
     

class WishlistSerializer(ModelSerializer):
    user = ReadOnlyField(source='WishList.user')
    prtoduct = ReadOnlyField(source='WishList.user')
    
    class Meta:
        model = WishList
        fields = '__all__'