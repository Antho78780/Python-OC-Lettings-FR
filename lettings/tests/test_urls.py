from django.urls import reverse, resolve
from lettings.models import Letting, Addres
from django.test import Client, TestCase


class TestUrls(TestCase):
    """La classe de TestUrls permet de tester toute les urls"""
    def setUp(self):
        """
        La méthode initialise une adresse,
        un client et une location pour les tests
        """
        self.client = Client()
        self.address = Addres.objects.create(
            number=5,
            street="l'oise",
            city="paris",
            state="france",
            zip_code=78567,
            country_iso_code="FRA")

        self.letting = Letting.objects.create(
            title="location1",
            address=self.address)

    def test_index_letting_url(self):
        """
        La méthode permet de tester le statut de
        la page et verifie le nom de de l'url
        """
        path = reverse('lettings_index')
        response = self.client.get(path)
        self.assertEqual(resolve(path).view_name, 'lettings_index')
        self.assertEqual(response.status_code, 200)

    def test_letting_url(self):
        """
        La méthode permet de tester le statut de la page,
        l'id de la location et verifie le nom de l'url
        """
        path = reverse('letting', kwargs={"letting_id": 1})
        response = self.client.get(path)
        self.assertEqual(resolve(path).view_name, 'letting')
        self.assertEqual(response.status_code, 200)
