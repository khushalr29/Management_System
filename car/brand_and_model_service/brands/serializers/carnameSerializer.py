from rest_framework import serializers
from shared.shared.models.brand_and_model_Service.carname import CarName
from shared.shared.models.enums import BodyType , FuelType , Transmission


class CarNameSerializer(serializers.ModelSerializer):
    body_type = serializers.ChoiceField(choices=BodyType.choices)
    fuel_type  = serializers.ChoiceField(choices=FuelType.choices)
    transmission = serializers.ChoiceField(choices=Transmission.choices)
    class Meta:
        model= CarName
        fields = "__all__"