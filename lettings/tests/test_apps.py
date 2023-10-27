from django.test import TestCase
from lettings.apps import LettingsConfig


class TestAppsName(TestCase):
    def test_apps(self):
        self.assertEqual(LettingsConfig.name, 'lettings')