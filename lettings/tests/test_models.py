from django.test import TestCase
from lettings.models import Letting, Addres

class TestModel(TestCase):
    """La classe TestModel permet de tester tous les models de l'application lettings"""
    def setUp(self):
        """La méthode initialise une adresse et une location de test"""
        self.address = Addres.objects.create(
            number=5,
            street="l'oise", 
            city="paris", 
            state="france", 
            zip_code=78567, 
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(
            title="location1", 
            address=self.address
        )
    
    def test_address_model(self):
        """La méthode permet de tester les informations de l'adresse"""
        expected_value = "5 l'oise"
        self.assertEqual(str(self.address), expected_value)
    
    def test_letting_model(self):
        """La méthode permet de tester les informations de l'adresse"""
        expected_value = "location1"
        self.assertEqual(str(self.letting), expected_value)

