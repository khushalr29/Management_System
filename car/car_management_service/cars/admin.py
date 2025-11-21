from django.contrib import admin
from .car import Car
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'brand',
        'model_name',
        'year',
        'price',
        'fuel_type',
        'available',
        'created_at',
        'updated_at',
        'deleted_at',
    ]
    search_fields = ('brand', 'model_name' , 'fuel_type','price',)
    readonly_fields =('created_at' , 'updated_at' , 'deleted_at',)
