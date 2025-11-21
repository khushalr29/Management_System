from django.db import models
from shared.models.base import BaseModel

class Brand(BaseModel):
    name = models.CharField(max_length=200 , unique=True)
    country = models.CharField(max_length=200 , blank=True , null=True)
    established_year = models.IntegerField(null=True , blank=True)
    
    def __str__(self):
        return f"{self.name} from {self.country}"
    

    