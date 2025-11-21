from rest_framework import serializers
from cars.emums import FuelType
from ..car import Car

class CarSerializer(serializers.ModelSerializer):
    fuel_type = serializers.ChoiceField(choices=FuelType.choices)
    class Meta:
        model = Car
        fields = '__all__'

