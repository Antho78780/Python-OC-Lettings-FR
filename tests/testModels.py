from django.test import TestCase
from profiles.models import Profile
from lettings.models import Letting, Addres
from django.contrib.auth.models import User
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
    
    def test_profiles(self):
        user = User.objects.create(username="antho")
        profile = Profile.objects.create(user= user, favorite_city="conflans")
        expected_value = "antho"
        assert str(profile) == expected_value


