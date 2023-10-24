from django.test import TestCase
from lettings.models import Letting, Addres

class TestModel(TestCase):
    def setUp(self):
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
        expected_value = "5 l'oise"
        self.assertEqual(str(self.address), expected_value)
    
    def test_letting_model(self):
        expected_value = "location1"
        self.assertEqual(str(self.letting), expected_value)

