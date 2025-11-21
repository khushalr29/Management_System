from rest_framework import serializers
from shared.shared.models.brand_and_model_Service.varients import Varients

class VarientsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Varients
        fields = "__all__"