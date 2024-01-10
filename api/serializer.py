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
    new_price=serializers.SerializerMethodField(read_only=True)
    client_name=serializers.SerializerMethodField(read_only=True)
    car_name=serializers.SerializerMethodField(read_only=True,source="books ")
    class Meta:
        model=Booking
        fields='__all__'
    
    def get_car_name(self,obj):
        return f"{obj.car_info}"
    def get_new_price(self,obj):
        if obj.discount:
            new_price=obj.price-obj.discount
            return new_price
        return obj.price
    def get_client_name(self,obj):
        if len(obj.client.other_name) > 1:
            return f"{obj.client.second_name.upper()},{obj.client.first_name} {obj.client.other_name}"
        return f"{obj.client.second_name.upper()},{obj.client.first_name}"
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=Reviews
        fields='__all__'
    

