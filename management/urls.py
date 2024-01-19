from django.urls import path
from .views import UserRegViewSet
from rest_framework import routers
from .views import UserRegView,UserLoginView


router=routers.DefaultRouter()
router.register('registration',UserRegViewSet,basename='registration')

urlpatterns = [
    path('register/',UserRegView,name='register'),
    path('login/',UserLoginView)
]

urlpatterns +=router.urls
