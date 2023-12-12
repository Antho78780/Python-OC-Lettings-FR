from django.test import TestCase
from oc_lettings_site.apps import OCLettingsSiteConfig


class TestAppsName(TestCase):
    def test_apps(self):
        self.assertEqual(OCLettingsSiteConfig.name, 'oc_lettings_site')
