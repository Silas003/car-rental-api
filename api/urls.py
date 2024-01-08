from django.urls import path
from .views import vehicles,add_vehicle,retrieve,delete
app_name="service"
urlpatterns=[
    path('add-vehicle',add_vehicle,name='add-vehicle'),
    path('get-vehicles',vehicles),
    path('<int:pk>',retrieve),
    path('delete/<int:pk>',delete),
]