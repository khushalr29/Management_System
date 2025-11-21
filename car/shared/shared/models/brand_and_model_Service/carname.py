from django.db import models
from shared.models.brand_and_model_Service.brand import Brand
from shared.models.base import BaseModel
from shared.models.enums import BodyType , FuelType , Transmission

class CarName(BaseModel):
    Brand = models.ForeignKey(Brand , on_delete=models.CASCADE , related_name="car_models")
    name = models.CharField(max_length=150)
    body_type = models.CharField(max_length=150 , choices=BodyType.choices , default="SUV")
    fuel_type = models.CharField(max_length=150 , choices=FuelType.choices , default="Petrol")
    transmission = models.CharField(max_length=150 , choices=Transmission.choices , default="Manual")
    engine_capacity = models.DecimalField(max_digits=5, decimal_places=2, null=True, help_text="Engine size in Litres")
    
    def __str__(self):
        return f"{self.name} and {self.engine_capacity}"

