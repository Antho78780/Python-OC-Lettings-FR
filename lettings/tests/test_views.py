from django.test import TestCase, Client
from lettings.models import Letting, Addres
from django.urls import reverse



class TestViews(TestCase):
    def setUp(self) :
        self.client = Client()
        self.address = Addres.objects.create(
            number=5,
            street="l'oise", 
            city="paris", 
            state="france", 
            zip_code=78567, 
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(
            title='location1', 
            address=self.address
        )

    def test_index_letting_view(self):
        response = self.client.get('/lettings/')
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_view(self):
       path = reverse('letting', kwargs={'letting_id': 1})
       response = self.client.get(path)
       self.assertTemplateUsed(response, 'lettings/letting.html')