
from .models import Carspec,Client,Booking,Reviews
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import CarSerializer,ClientSerializer,ReviewSerializer,Booking,BookingSerializer
from rest_framework import status
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.views import LoginView
from drf_yasg.utils import swagger_auto_schema
from django.core.mail import EmailMessage
from django.http import HttpResponse

def send_html_email_view(request:Request):
    books=Booking.objects.all()
    for user in books:
        
        if user.end_date-user.start_date:
            # print('its not deadline yet')
            # print(user.client.email,user.end_date-user.start_date)
            continue
        else:
            
            subject = 'Car Rental Deadline'
            body = f'Dear {user.client}, we wish to inform you the deadline of your booking'
            from_email = 'silaskumi4@gmail.com'
            to_email = [user.client.email]

            email = EmailMessage(subject, body, from_email, to_email)
            email.content_subtype = 'html'  # Set the content type to HTML
            email.send()

    return HttpResponse("HTML Email sent successfully.")
class GoogleLogin(LoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client


@api_view(['GET','POST'])
@swagger_auto_schema()
def list_vehicles(request : Request):
    
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
    queryset=Client.objects.all()


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class=ReviewSerializer
    queryset=Reviews.objects.all()


class BookingViewset(viewsets.ModelViewSet):
    serializer_class=BookingSerializer
    queryset=Booking.objects.all()