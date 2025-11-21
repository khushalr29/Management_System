from django.contrib import admin
from shared.shared.models.brand_and_model_Service.brand import Brand
from shared.shared.models.brand_and_model_Service.carname import CarName
from shared.shared.models.brand_and_model_Service.varients import Varients
from django.contrib import admin 

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'id' , 
        'name' , 
        'country',
        'established_year' ,
        'created_at',
        'updated_at',
        'deleted_at',
    ]
    search = ['name', 'country' , 'established_year']
    readonly_fields= ['created_at' , 'updated_at' , "deleted_at"]

@admin.register(CarName)
class CarNameAdmin(admin.ModelAdmin):
    list_display =[
        'id',
        'Brand',
        'name',
        'body_type',
        'fuel_type',
        'transmission',
        'engine_capacity',
        'created_at',
        'updated_at',
        'deleted_at',
    ]
    search = ['Brand','name', 'body_type' , 'fuel_type' , 'transmission' , 'engine_capacity' ]
    readonly_fields= ['created_at' , 'updated_at' , "deleted_at"]

 
@admin.register(Varients)
class ViarentsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "car_model",
        'name',
        'price',
        "seating_capacity",
        'mileage',
        'features',
        'is_active',
        'created_at',
        'updated_at',
        'deleted_at',
    ]
    search_fields = ['car_model' , 'name' , 'price' , 'seating_capacity'  , 'mileage' ,'features' , 'is_active' ]
    readonly_fields= ['created_at' , 'updated_at' , "deleted_at"]

