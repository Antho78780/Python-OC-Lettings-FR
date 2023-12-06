from django.test import TestCase
from lettings.apps import LettingsConfig


class TestAppsName(TestCase):
    """La classe de TestAppsName permet de tester le nom de l'application"""
    def test_apps(self):
        self.assertEqual(LettingsConfig.name, 'lettings')