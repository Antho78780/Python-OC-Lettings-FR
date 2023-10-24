from django.test import TestCase
from lettings.models import Letting, Addres
import pytest


@pytest.mark.django_db
class TestModel(TestCase):
    def test_modelAdress(self):
        address = Addres.objects.create(number=5, street="l'oise", city="paris", state="france", zip_code=78567, country_iso_code="FRA")
        expected_value = "5 l'oise"
        assert str(address) == expected_value
    
    def test_modelLetting(self):
        address = Addres.objects.create(number=5, street="l'oise", city="paris", state="france", zip_code=78567, country_iso_code="FRA")
        letting = Letting.objects.create(title="location1", address=address)
        expected_value = "location1"
        assert str(letting) == expected_value
