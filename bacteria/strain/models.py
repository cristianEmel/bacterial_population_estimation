from django.db import models

from django.contrib.auth.models import User


class StrainModel(models.Model):

    """
        This model is used to store the Strains of the database
    """

    #Days that the bacteria needs to mature
    days_of_maturation: int = models.IntegerField()
    #Life expectancy of the bacteria
    life_expectancy: int = models.IntegerField()
    #Reproduction rate of the bacteria
    reproduction_rate: int = models.IntegerField()
    #User owner of the strain
    user:User = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table:str = 'strain'