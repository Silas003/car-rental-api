from django.db import models

# Create your models here.
fuel_choices=(
    ("Diesel","Diesel"),
    ("Super","Super")
)

trans_choices=(
    ("Automatic","Automatic"),
    ("Manual","Manual")
)

id_choices=(
    ("Ghana Card","Ghana Card"),
   ( "Voters ID","Voters ID"),
   ("NHIS","NHIS"),
   ("Driver License","Driver License")
)
status_choice=(
    ("Available","Available"),
    ("Unavailable","Unavailable")
)
booking_status_choice=(
    ("Completed","Complete"),
    ("Reserved","Reserved"),
    ("Cancelled","Cancelled")
)

class Carspec(models.Model):
    car_brand=models.CharField(max_length=50)
    car_model=models.CharField(max_length=100)
    production_year=models.CharField(max_length=50)
    mileage=models.FloatField()
    color=models.CharField(max_length=50,default=None)
    fuel_type=models.CharField(max_length=20,choices=fuel_choices)
    transmission_type=models.CharField(max_length=20,choices=trans_choices)
    status=models.CharField(max_length=100,choices=status_choice)
    DV_Number=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return f"{self.car_brand} { self.car_model}"


class Client(models.Model):
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    other_name=models.CharField(max_length=100,default=None)
    phone=models.CharField(unique=True,max_length=14)
    client_Id_type=models.CharField(max_length=100,choices=id_choices)
    client_id=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='client_images')
    email=models.EmailField()
    
    def __str__(self):
        return f"{self.second_name.upper()} {self.first_name} "
class Booking(models.Model):
    car_info=models.ForeignKey(Carspec,on_delete=models.SET_NULL,related_name='books',null=True)
    client=models.ForeignKey(Client,on_delete=models.PROTECT)
    start_date=models.DateField()
    end_date=models.DateField()
    price=models.DecimalField( max_digits=15, decimal_places=2)
    discount=models.DecimalField(max_digits=15, decimal_places=2)
    status=models.CharField(max_length=100,choices=booking_status_choice)


class Reviews(models.Model):
    user_id=models.ForeignKey(Client,on_delete=models.DO_NOTHING)
    car_id=models.ForeignKey(Carspec,on_delete=models.DO_NOTHING)
    review=models.TextField(max_length=1000)


class Nothing(models.Model):
    pass