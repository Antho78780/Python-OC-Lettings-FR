from pytest_django.asserts import assertTemplateUsed
import pytest
from profiles.models import Profile
from django.test import Client, TestCase

@pytest.mark.django_db
class TestView(TestCase):
    client = Client()

    def test_indexProfile(self):
        response = self.client.get('/profiles/')
        assertTemplateUsed(response, "profiles/index.html")
        assert response.status_code == 200
    
    def test_profiles(self):
        pass



