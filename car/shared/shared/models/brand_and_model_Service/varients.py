from django.db import models
from shared.models.base import BaseModel
from shared.models.brand_and_model_Service.carname import CarName

class Varients(BaseModel):
    car_model = models.ForeignKey(CarName , on_delete=models.CASCADE , related_name="Car_varient")
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    seating_capacity = models.PositiveIntegerField(default=5)
    mileage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    features = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    