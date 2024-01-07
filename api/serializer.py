from rest_framework import serializers
from .models import Carspec

class CarSerializer(serializers.ModelSerializer):
    #url=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Carspec
        fields=['car_brand','car_model','car_body']
    
    # def get_url(self,obj):
    #     return f"localhost:8000/{obj.id}"