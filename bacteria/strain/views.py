from typing import Dict, List

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import json

from .bacterie import Bacteria, Strain
from .models import StrainModel
from .serializers import StrainCountSerializer, StrainSerializer


class StrainViewSet(ModelViewSet):

    """
        This class create a crud of the model StrainModel
    """

    serializer_class = StrainSerializer
    queryset = StrainModel.objects.all()

@api_view(['POST'])
def population(request):

    """
        This method returns the number of bacteria that will exist after a certain number of days.

        :param days_of_maturation: Days of maturation
        :type days_of_maturation: int
        :param life_expectancy: Life expectancy
        :type life_expectancy: int
        :param reproduction_rate: Reproduction rate
        :type reproduction_rate: int
        :param bacteria: List of bacteria life expectancies
        :type bacteria: List[int]
        :param days: Number of days
        :type days: int

        :return: Number of bacteria
        :rtype: int
    """

    try:

        #Validate the params
        data: Dict[str, int] = request.data
        serializer = StrainCountSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        #Extract the values
        strain: int = data.get('strain')
        days: int = data.get('days')
        bacteria: List[int] = data.get('bacteria')

        strain_instance: StrainModel = StrainModel.objects.get(id=strain)

        days_of_maturation: int = strain_instance.days_of_maturation
        life_expectancy: int = strain_instance.life_expectancy
        reproduction_rate: int = strain_instance.reproduction_rate

        #Create the bacteria definition
        bacteria_def: Bacteria = Bacteria(days_of_maturation, life_expectancy, reproduction_rate)
        #Create the bacteria strains
        bacteria_strains: List[Strain] = list(map(lambda days_for_replication: Strain(days_for_replication, bacteria_def), bacteria))

        #Iterate over the days
        for _ in range(days):
            #Create a list for the new bacteria
            new_bacteria: List[Strain] = []
            #Iterate over the bacteria strains
            for bac in bacteria_strains:

                #Check if the bacteria is ready to replicate
                if bac.is_time_of_replication():
                    #Add the new bacteria to the list
                    new_bacteria.extend(bac.replicate())
                else:
                    #Age the bacteria
                    bac.age()

            #Add the new bacteria to the list of bacteria strains
            bacteria_strains.extend(new_bacteria)

        response = Response(
            {
                'population': len(bacteria_strains)
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        response = Response(
            {
                'error': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    return response
