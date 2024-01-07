
from .models import Carspec
from rest_framework.decorators import api_view,permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import JsonResponse

from .serializer import CarSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def home(request : Request):
    if request.method=="GET":
        try:
            if request.query_params:
                brand=request.query_params['car_brand']
                car=Carspec.objects.get(car_brand=brand)
                serializer=CarSerializer(car)
                return Response(serializer.data) 
        except AttributeError as e:
            print(e)
        serializer=CarSerializer(Carspec.objects.all(),many=True)    
        return Response(serializer.data)
    if request.method=="POST":
        if request.data:
            data=request.data
            print("not bad")
            return Response({"new_ message":data})
        else:
            print("you suck")

@api_view(['POST'])
def post(request:Request):
    data=request.data
    #print(data)
    car=Carspec.objects.create(car_brand=data['car_brand'],car_model=data['car_model'])
    car.save()
    print(car)
    serializer=CarSerializer(car)
    return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['PUT','GET'])
def retrieve(request:Request,pk):

    car=Carspec.objects.get(id=pk)
    data=request.data 
    if request.method=="PUT" :     
        print(data)  
        car.car_brand=data['car_brand'] 
        car.car_model=data['car_model']
        car.save()
        serializer=CarSerializer(car)
        return Response(serializer.data)
   
    serializer=CarSerializer(car)
    return Response(serializer.data)

@api_view(['GET','DELETE'])
def delete(request:Request,pk):
    car=Carspec.objects.get(id=pk)
    if request.method=="DELETE":    
        car.delete()
        return Response({"message":"car deleted"},status=status.HTTP_204_NO_CONTENT)
    serializer=CarSerializer(car)
    return Response(serializer.data)