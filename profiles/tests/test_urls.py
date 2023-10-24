from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile

class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(
            username="Antho"
        )
        Profile.objects.create(
            user=user, 
            favorite_city='Maurecourt'
        )
        
    def test_index_profiles_url(self):
        path = reverse('profiles_index')
        response = self.client.get(path)
        self.assertEqual(resolve(path).view_name, 'profiles_index')
        self.assertEqual(response.status_code, 200)
    
    def test_profile_url(self):
        path = reverse('profile', kwargs={'username': 'Antho'})
        response = self.client.get(path)
        self.assertEqual(resolve(path).view_name, 'profile')
        self.assertEqual(response.status_code, 200)