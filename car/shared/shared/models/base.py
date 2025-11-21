from django.db import models

class BaseModel(models.Model):
    created_at= models.DateTimeField(null=True , blank=True)
    updated_at = models.DateTimeField(null=True , blank=True)
    deleted_at= models.DateTimeField(null=True , blank=True)
    
