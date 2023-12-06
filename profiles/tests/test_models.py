from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User

class TestModel(TestCase):
    """La classe TestModel permet de tester tous les models de l'application profile"""
    def setUp(self):
        """La méthode initialise un utilisateur et un profile"""
        self.user = User.objects.create(
            username="Antho"
        )
        self.profile = Profile.objects.create(
            user=self.user, 
            favorite_city="maurecourt"
        )

    def test_profile_model(self):
        """La méthode permet de tester le profile"""
        expected_value = "Antho"
        self.assertEqual(str(self.profile), expected_value)
