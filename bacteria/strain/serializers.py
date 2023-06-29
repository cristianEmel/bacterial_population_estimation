from rest_framework import serializers
from .models import StrainModel


class StrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrainModel
        fields = '__all__'

    def validate(self, data):
        for field_name, value in data.items():
            if field_name in ["days_of_maturation", "reproduction_rate"] and value <= 0:
                raise serializers.ValidationError(f"{field_name} must be greater than 0")
            if field_name == "life_expectancy" and value < 1:
                raise serializers.ValidationError(f"{field_name} must be greater than or equal to 1")
        return data


class StrainCountSerializer(serializers.Serializer):
    strain = serializers.IntegerField(min_value=1)
    days = serializers.IntegerField(min_value=1)
    bacteria = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_bacteria(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("At least one bacteria are required")
        return value
    def validate_strain(self, value):
        value = StrainModel.objects.get(id=value)
        if not value:
            raise serializers.ValidationError("Strain is not valid")

        return value

    