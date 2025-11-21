from django.db import models

class FuelType(models.TextChoices):
    PETROL= 'Petrol' 
    DIESEL= 'Diesel'
    ELECTRIC='Electric'
    HYBRID='Hybrid'
    