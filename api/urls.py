from django.urls import path
from .views import home,post,retrieve,delete
urlpatterns=[
    path('api',post,name='post'),
    path('home',home),
    path('<int:pk>',retrieve),
    path('delete/<int:pk>',delete),
]