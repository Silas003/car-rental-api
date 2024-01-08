from django.contrib import admin
from .models import Carspec,Client,Reviews,Booking

@admin.register(Carspec)
class CarspecAdmin(admin.ModelAdmin):
    list_display=['car_brand','car_model','production_year','status']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display=['first_name','second_name','client_Id_type']


@admin.register(Booking)
class ClientAdmin(admin.ModelAdmin):
    list_display=['car_info','client','status']


@admin.register(Reviews)
class CarspecAdmin(admin.ModelAdmin):
    list_display=['user_id','review']
