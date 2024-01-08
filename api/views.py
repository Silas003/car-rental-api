
from .models import Carspec,Client,Booking,Reviews
from rest_framework.decorators import api_view,permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import CarSerializer,ClientSerializer,ReviewSerializer,Booking,BookingSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def list_vehicles(request : Request):
    if request.method=="GET":


        # try:
        #     if request.query_params:
        #         brand=request.query_params['car_brand']
        #         car=Carspec.objects.get(car_brand=brand)
        #         serializer=CarSerializer(car)
        #         return Response(serializer.data) 
        # except AttributeError as e:
        #     print(e)
        
        
        for auth in Carspec.objects.all():
            car_booking = auth.books.all()

        # Check if any booking has status "Reserved"
            if any(book.status == "Reserved" for book in car_booking):
                auth.status = "Unavailable"
            else:
                auth.status = "Available"

            auth.save()

    # Serialize the updated data after the loop
    serializer = CarSerializer(Carspec.objects.all(), many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def add_vehicle(request:Request):
    data=request.data
    
    car=Carspec.objects.create(
        car_brand=data['car_brand'],
        car_model=data['car_model'],
        production_year=data['production_year'],
        mileage=data['mileage'],
        color=data['color'],
        fuel_type=data['fuel_type'],
        transmission_type=data['transmission_type'],
        status=data['status'],
        DV_Number=data['DV_Number'])
    car.save()
    
    serializer=CarSerializer(car)
    return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['PUT','GET'])
def retrieve_vehicle(request:Request,pk):

    car=Carspec.objects.get(id=pk)
    data=request.data 
    if request.method=="PUT" :     
        print(data)  
        car.car_brand=data['car_brand'] 
        car.car_model=data['car_model']
        car.production_year=data['production_year']
        car.mileage=data['mileage']
        car.color=data['color']
        car.fuel_type=data['fuel_type']
        car.transmission_type=data['transmission_type']
        car.status=data['status']
        car.DV_Number=data['DV_Number']
        car.save()
        serializer=CarSerializer(car)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
   
    serializer=CarSerializer(car)
    return Response(serializer.data)

@api_view(['GET','DELETE'])
def delete_vehicle(request:Request,pk):
    car=Carspec.objects.get(id=pk)
    if request.method=="DELETE":    
        car.delete()
        return Response({"message":"vehicle removed from inventory successfully"},status=status.HTTP_204_NO_CONTENT)
    serializer=CarSerializer(car)
    return Response(serializer.data)


class ClientViewset(viewsets.ModelViewSet):
    serializer_class=ClientSerializer
    queryset=Client.objects.all()


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class=ReviewSerializer
    queryset=Reviews.objects.all()