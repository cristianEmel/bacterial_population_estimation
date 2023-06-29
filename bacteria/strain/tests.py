from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import StrainModel
from django.contrib.auth.models import User
import json


class StrainViewSetTestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        # Create a strain
        self.strain = StrainModel.objects.create(
            days_of_maturation=20,
            life_expectancy=5,
            reproduction_rate=50,
            user=self.user
        )

    def test_list_strains(self):

        """
            This method test the list of strains
        """

        # Get the url
        url: str = reverse("strain-list")
        response = self.client.get(url)
        #The response must be 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Dont must create a new strain
        self.assertEqual(len(response.data), 1)

    def test_create_strain(self):

        """
            This method test the creation of a strain
        """

        # Get the url
        url = reverse("strain-list")
        data = {
            "days_of_maturation": 5,
            "life_expectancy": 5,
            "reproduction_rate": 3,
            "user": self.user.id
        }
        response = self.client.post(url, data)
        #The response must be 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Must create a new strain
        self.assertEqual(StrainModel.objects.count(), 2)

        data = {
            "days_of_maturation": -1,
            "life_expectancy": 5,
            "reproduction_rate": 3,
            "user": self.user.id
        }
        response = self.client.post(url, json=data, content_type='application/json')
        #Dont must create a new strain with negative days of maturation
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        #The quantity of strains must be 2
        self.assertEqual(StrainModel.objects.count(), 2)


class PopulationViewTestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        # Create a strain
        self.strain = StrainModel.objects.create(
            days_of_maturation=1,
            life_expectancy=3,
            reproduction_rate=2,
            user=self.user
        )

    def test_population_view(self):

        """
            This method test the population view
        """
        # Get the url
        url = reverse("count_replication")

        data = {
            "strain": self.strain.id,
            "days": 8,
            "bacteria": [2,3,3,1,2],
        }
        json_data = json.dumps(data)
        response = self.client.post(url, json_data, content_type='application/json')
        #The response must be 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #The population must be 37
        self.assertIn('population', response.data)
        self.assertEqual(response.data["population"], 37)