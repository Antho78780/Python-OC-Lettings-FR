from django.test import TestCase
from profiles.apps import ProfilesConfig


class TestAppsName(TestCase):
    def test_apps(self):
        self.assertEqual(ProfilesConfig.name, 'profiles')
