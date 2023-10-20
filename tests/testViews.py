from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest
from lettings.models import Letting, Addres
from profiles.models import Profile
from django.test import Client, TestCase

@pytest.mark.django_db
class TestView(TestCase):
    client = Client()

    def test_indexLetting(self):
        response = self.client.get('/lettings/')
        assertTemplateUsed(response, 'lettings/index.html')
        assert response.status_code == 200

    def test_letting(self):
        address = Addres.objects.create(number=5, street="l'oise", city="paris", state="france", zip_code=78567, country_iso_code="FRA")
        letting = Letting.objects.create(title="location1", address=address)
        path = reverse('letting', kwargs={"letting_id": 1})
        response = self.client.get(path)
        self.assertEqual(path, '/lettings/1/')
        assertTemplateUsed(response, 'lettings/letting.html')
        assert response.status_code == 200

    def test_indexProfile(self):
        response = self.client.get('/profiles/')
        assertTemplateUsed(response, "profiles/index.html")
        assert response.status_code == 200
    
    def test_profiles(self):
        pass



