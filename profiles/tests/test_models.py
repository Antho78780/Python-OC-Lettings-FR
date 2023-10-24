from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User
import pytest

class TestModel(TestCase):
    @pytest.mark.django_db
    def test_modelProfiles(self):
        pass
