from typing import List

class Bacteria:

    """
        This class represents a bacteria definition.
    """

    def __init__(self, days_of_maturation: int, life_expectancy: int, reproduction_rate: int) -> None:

        """
            This method initializes the class.

            :param days_of_maturation: Days of maturation
            :type days_of_maturation: int
            :param life_expectancy: Life expectancy
            :type life_expectancy: int
            :param reproduction_rate: Reproduction rate
            :type reproduction_rate: int
        """

        #Set the value of days_of_maturation, life_expectancy and reproduction_rate
        self.days_of_maturation: int = days_of_maturation
        self.life_expectancy: int = life_expectancy
        self.reproduction_rate: int = reproduction_rate

class Strain:

    """
        This class represents a bacteria strain.
    """

    def __init__(self, days_for_replication: int, bacteria: Bacteria) -> None:

        """
            This method initializes the class.

            :param days_for_replication: Days for replication
            :type days_for_replication: int
            :param bacteria: Bacteria
            :type bacteria: Bacteria
        """

        #Set the value of days_for_replication and bacteria
        self.bacteria: Bacteria = bacteria
        self.days_for_replication: int = days_for_replication

    def is_time_of_replication(self) -> bool:

        """
            This method returns True if the bacteria is ready to replicate, False otherwise.

            :return: Is time of replication ?
            :rtype: bool

        """

        return self.days_for_replication == 0 and self.days_for_replication <= self.bacteria.life_expectancy
    
    def new_strain(self):

        """
            This method returns a new strain.

            :return: New strain
            :rtype: Strain

        """

        return Strain(self.bacteria.days_of_maturation + self.bacteria.life_expectancy, self.bacteria)
    
    def replicate(self) -> List:

        """
            This method returns a list of strains that are the result of the replication.

            :return: List of strains
            :rtype: List[strains]

        """

        #Restart the counter of the days for replication
        self.days_for_replication: int = self.bacteria.life_expectancy

        return [self.new_strain() for _ in range(self.bacteria.reproduction_rate)]
    
    def age(self) -> None:

        """
            This method ages the bacteria.

        """
        self.days_for_replication -= 1

