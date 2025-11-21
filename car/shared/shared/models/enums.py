from django.db import models

class FuelType(models.TextChoices):
    PETROL= 'Petrol' 
    DIESEL= 'Diesel'
    ELECTRIC='Electric'
    HYBRID='Hybrid'
    

class BodyType(models.TextChoices):
    SUV = "SUV", "SUV"
    SEDAN = "Sedan", "Sedan"
    HATCHBACK = "Hatchback", "Hatchback"
    TRUCK = "Truck", "Truck"
    COUPE = "Coupe", "Coupe"
    VAN = "Van", "Van"

class Transmission(models.TextChoices):
    MANUAL = 'Manual'
    AUTOMATIC='Automatic', 'Automatic'      