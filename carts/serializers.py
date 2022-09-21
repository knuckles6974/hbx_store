from products.models import Product
from users.models    import User
from rest_framework  import serializers

class ProductSereializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fileds = ['id','name','size','price']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','phone_number']

        


