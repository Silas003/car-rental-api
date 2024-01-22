
from .models import Carspec,Client,Booking,Reviews
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import CarSerializer,ClientSerializer,ReviewSerializer,Booking,BookingSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from .tasks import send_mail_func


def send_html_email_view(request:Request):
    

    send_mail_func.delay()
    # books=Booking.objects.all()
    # for user in books:
        
    #     if user.end_date-user.start_date:
    #         # print('its not deadline yet')
    #         # print(user.client.email,user.end_date-user.start_date)
    #         continue
    #     else:
            
    #         subject = 'Car Rental Deadline'
    #         body = f'Dear {user.client}, we wish to inform you the deadline of your booking'
    #         from_email = 'silaskumi4@gmail.com'
    #         to_email = [user.client.email]

    #         email = EmailMessage(subject, body, from_email, to_email)
    #         email.content_subtype = 'html'  # Set the content type to HTML
    #         email.send()

    return HttpResponse("Email delivered.")

@api_view(['GET','POST'])
@swagger_auto_schema()
def list_vehicles(request : Request):
    car_brand=request.query_params.get('car_brand')
    car_model=request.query_params.get('car_model')
    prod_year=request.query_params.get('prod_year')
    search=request.query_params.get('search')
   
    if request.method=="GET":
        for auth in Carspec.objects.all():
            car_booking = auth.books.all()

        # Check if any booking has status "Reserved"
            if any(book.status == "Reserved" for book in car_booking):
                auth.status = "Unavailable"
            else:
                auth.status = "Available"

            auth.save()

    # Serialize the updated data after the loop
    filter_params = {}
    if car_brand:
        filter_params['car_brand'] = car_brand
    if car_model:
        filter_params['car_model'] = car_model
    if prod_year:
        filter_params['production_year'] = prod_year

    filtered_list = Carspec.objects.filter(**filter_params)
    if car_brand or car_model or prod_year:
        serializer=CarSerializer(filtered_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if search:
        searched_list=Carspec.objects.filter(car_brand__icontains=search)
        serializer=CarSerializer(searched_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    serializer = CarSerializer(Carspec.objects.all(), many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
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


@swagger_auto_schema()
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


@permission_classes([permissions.IsAdminUser])
@swagger_auto_schema()
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
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    queryset=Client.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['first_name','second_name','phone']

class ReviewViewset(viewsets.ModelViewSet):
    serializer_class=ReviewSerializer
    queryset=Reviews.objects.all()
    

class BookingViewset(viewsets.ModelViewSet):
    serializer_class=BookingSerializer
    queryset=Booking.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['car_info','status','start_date']