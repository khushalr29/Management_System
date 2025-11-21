from rest_framework import serializers
from shared.shared.models.brand_and_model_Service.brand import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields = "__all__"