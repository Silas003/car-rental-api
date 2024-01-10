from django.urls import path
from .views import list_vehicles,add_vehicle,retrieve_vehicle,delete_vehicle,ClientViewset,ReviewViewset,BookingViewset
from rest_framework import routers


app_name="service"
urlpatterns=[
    path('add-vehicle',add_vehicle,name='add-vehicle'),
    path('list-vehicles',list_vehicles),
    path('<int:pk>',retrieve_vehicle),
    path('delete/<int:pk>',delete_vehicle),
    
]

router=routers.DefaultRouter()
router.register("client",ClientViewset,basename='client')
router.register("reviews",ReviewViewset,basename='reviews')
router.register("booking",BookingViewset,basename='booking')

urlpatterns+=router.urls