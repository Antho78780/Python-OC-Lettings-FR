from django.urls import reverse, resolve
from lettings.models import Letting, Addres
from django.test import Client, TestCase

class TestView(TestCase):
    def setUp(self):
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
        path = reverse('lettings_index')
        response = self.client.get(path)
        self.assertEqual(resolve(path).view_name, 'lettings_index')
        self.assertEqual(response.status_code, 200)

    def test_letting_url(self):
        path = reverse('letting', kwargs={"letting_id": 1})
        response = self.client.get(path)
        self.assertEqual(resolve(path).view_name, 'letting')
        self.assertEqual(response.status_code, 200)



