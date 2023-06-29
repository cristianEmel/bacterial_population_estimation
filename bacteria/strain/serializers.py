from rest_framework import serializers
from .models import StrainModel
from typing import List


class StrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrainModel
        fields = '__all__'

    def validate_days_of_maturation(self, value: int) -> int:

        """
            Validate that the days of maturation is greater than 0

            :param value: Days of maturation
            :type value: int
            :return: Days of maturation
            :rtype: int
        """

        if value <= 0:
            raise serializers.ValidationError("Days of maturation must be greater than 0")
        return value
    
    def validate_life_expectancy(self, value: int) -> int:
            
        """
            Validate that the life expectancy is greater than or equal to 1

            :param value: Life expectancy
            :type value: int
            :return: Life expectancy
            :rtype: int
        """

        if value < 1:
            raise serializers.ValidationError("Life expectancy must be greater than or equal to 1")
        return value
    
    def validate_reproduction_rate(self, value: int) -> int:
            
        """
            Validate that the reproduction rate is greater than 0

            :param value: Reproduction rate
            :type value: int
            :return: Reproduction rate
            :rtype: int
        """

        if value <= 0:
            raise serializers.ValidationError("Reproduction rate must be greater than 0")
        return value

class StrainCountSerializer(serializers.Serializer):
    strain: int = serializers.IntegerField(min_value=1)
    days:int  = serializers.IntegerField(min_value=1)
    bacteria: List[int] = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_bacteria(self, value) -> List[int]:

        """
            Validate that the list of bacteria is not empty

            :param value: List of bacteria
            :type value: List[int]
            :return: List of bacteria
            :rtype: List[int]
        """

        if len(value) < 1:
            raise serializers.ValidationError("At least one bacteria are required")
        return value
    
    def validate_strain(self, value) -> int:

        """
            Validate that the strain exists

            :param value: Strain
            :type value: int
            :return: int
            :rtype: int
        """

        if not StrainModel.objects.filter(id=value).exists():
            raise serializers.ValidationError("Strain is not valid")

        return value

    