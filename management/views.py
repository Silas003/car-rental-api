from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import CustomUser,UserRegSerializer,UserLoginSerializer
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth.models import User
    
class UserRegViewSet(viewsets.ModelViewSet):
    serializer_class=UserRegSerializer
    permission_classes=[AllowAny]
    queryset=CustomUser.objects.all()

@method_decorator(csrf_exempt, name='dispatch')
@permission_classes([AllowAny])
@api_view(['POST'])
def UserRegView(request:Response):
        if request.method == 'POST':
            data = request.POST  # Use request.POST for form data or request.body for raw data
            email = data.get('email')
            password = data.get('password')

            # Create a User object without saving it to the database
            user = User(email=email)
            user.set_password(password)  # Set the hashed password

            serializer = UserRegSerializer(data=data)

            if serializer.is_valid():
                # Save the user with the hashed password
                user.save()
                return Response({
                    "message":f'account created successfully for {email}',
                    
                },status=status.HTTP_201_CREATED)
            else:
                return serializer.errors
            
            
@api_view(['POST'])
@permission_classes([AllowAny])
def UserLoginView(request:Request):
    serializer=UserLoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        tokens=serializer.create_token(serializer.validated_data)
        return Response(
            {
                "message":"user login successful",
                
                'keys':tokens
            }
        )