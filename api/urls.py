from django.urls import path
from .views import list_vehicles,add_vehicle,retrieve_vehicle,delete_vehicle,ClientViewset,ReviewViewset,BookingViewset,GoogleLogin,send_html_email_view
from rest_framework import routers


app_name="service"
urlpatterns=[
    path('add-vehicle',add_vehicle,name='add-vehicle'),
    path('mail',send_html_email_view,name='mail'),
    path('list-vehicles',list_vehicles),
    path('<int:pk>',retrieve_vehicle),
    path('delete/<int:pk>',delete_vehicle),
    path('auth/social/google/', GoogleLogin.as_view(), name='google_login'),
    
]

router=routers.DefaultRouter()
router.register("client",ClientViewset,basename='client')
router.register("reviews",ReviewViewset,basename='reviews')
router.register("booking",BookingViewset,basename='booking')

urlpatterns+=router.urls