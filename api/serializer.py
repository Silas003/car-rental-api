from rest_framework import serializers
from .models import Carspec,Client,Reviews,Booking

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Carspec
        fields='__all__'



class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Client
        fields='__all__'
    

class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Booking
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=Reviews
        fields='__all__'
    

