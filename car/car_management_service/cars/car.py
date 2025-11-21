from django.db import models
from cars.emums import FuelType

class Car(models.Model):    
    brand= models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    fuel_type= models.CharField(max_length=20 , choices = FuelType.choices , default=FuelType.DIESEL)
    available = models.BooleanField(default=True)
    created_at= models.DateTimeField(null=True , blank=True)
    updated_at= models.DateTimeField(null=True , blank=True)
    deleted_at = models.DateTimeField(null=True , blank=True)

    def __str__(self):
        return f"{self.brand} {self.model_name} { self.year}"


