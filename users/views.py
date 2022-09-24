
#import re

from rest_framework import generics

from django.contrib.auth.hashers import make_password
from rest_framework  import status
from rest_framework.response  import Response
#from rest_framework.views  import APIView
from .models         import User
from .serializers    import UserSerializer #WishlistSerializer

# Create your views here.

# REGEX_EMAIL = "^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
# REGEX_PASSWORD = "^(?=.{8,16}$)(?=.*[a-z])(?=.*[0-9]).*$"

class SignupView(generics.CreateAPIView):
    
    #permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    
       
    def Signup(self,request):
        
        data = request.data
        #token = Token.objects.create(username=data['username'], )
        
        data['password'] = make_password(data['password'])
        qs = User.objects.filter(email=request.data['email'])
     
        if qs.exists():
            return Response({"message": "ALREADY EXIST"},
        status = status.HTTP_400_BAD_REQUEST)
        
        # if not re.match(REGEX_EMAIL, request.data['email']):
        #     return Response({"message":"BAD REQUEST"},
        # status = status.HTTP_400_BAD_REQUEST)

        # if not re.match(REGEX_PASSWORD, request.data['password']):
        #     return Response({"message":"BAD REQUEST"},
        # status = status.HTTP_400_BAD_REQUEST)
              
            
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            
        return Response({"message":"SUCCESS"}, status=status.HTTP_201_CREATED)    
                
        
        
    
    
    
    
    
    