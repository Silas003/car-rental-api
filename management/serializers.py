from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'is_superuser']
        ordering = ('-email')

    def validate(self, attrs):
        email = attrs['email']
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Account already exists")
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_superuser=validated_data['is_superuser']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)
    class Meta:
        model=CustomUser
        fields=['email','password']
    def validate(self, attrs):
        if not CustomUser.objects.filter(email=attrs["email"]):
            raise serializers.ValidationError("User Does Not Exist!")
        return attrs
    
    def create_token(self,attrs):
        user = authenticate(email=attrs["email"],password=attrs["password"])
        if not user:
            raise serializers.ValidationError("Invalid Credentials")
        
        refresh = RefreshToken.for_user(user)

        
        token_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # print(attrs)

        # user_data = {
        #     "user_id":user.id,
        #     "username":user.username
        # }

        # token_data["user"] = user_data

        return token_data
    