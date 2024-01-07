from django.contrib import admin
from .models import Carspec
# Register your models here.

#admin.site.register(Carspec)

@admin.register(Carspec)
class CarspecAdmin(admin.ModelAdmin):
    list_display=['car_brand','car_model','production_year']