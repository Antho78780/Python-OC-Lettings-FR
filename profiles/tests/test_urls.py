from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile

class TestUrls(TestCase):
    """La classe TestUrls permet de tester les urls index et profile"""
    def setUp(self):
        """La méthode initialise un utilisateur et un profile"""
        self.client = Client()
        user = User.objects.create(
            username="Antho"
        )
        Profile.objects.create(
            user=user, 
            favorite_city='Maurecourt'
        )
        
    def test_index_profiles_url(self):
        "La méthode permet de tester le nom de l'url et le code status"
        path = reverse('profiles_index')
        response = self.client.get(path)
        self.assertEqual(resolve(path).view_name, 'profiles_index')
        self.assertEqual(response.status_code, 200)
    
    def test_profile_url(self):
        "La méthode permet de tester le nom de l'url, l'id de l'utilisateur et le code status"
        path = reverse('profile', kwargs={'username': 'Antho'})
        response = self.client.get(path)
        self.assertEqual(resolve(path).view_name, 'profile')
        self.assertEqual(response.status_code, 200)