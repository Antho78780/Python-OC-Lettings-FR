from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User

class TestModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Antho"
        )
        self.profile = Profile.objects.create(
            user=self.user, 
            favorite_city="maurecourt"
        )

    def test_profile_model(self):
        expected_value = "Antho"
        self.assertEqual(str(self.profile), expected_value)
