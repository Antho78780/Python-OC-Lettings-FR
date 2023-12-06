from profiles.models import Profile
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class TestView(TestCase):
    """La classe TestView permet de tester les views index et profiles"""
    client = Client()
    def test_indexProfile(self):
        """La méthode permet de tester la template index.html"""
        response = self.client.get('/profiles/')
        self.assertTemplateUsed(response, "profiles/index.html")
    
    def test_profiles(self):
        """La méthode permet de tester la template profile.html, l'ajout d'un profile et d'un utilisateur"""
        user = User.objects.create(username='Antho')
        profile = Profile.objects.create(user=user, favorite_city='maurecourt')
        path = reverse('profile', kwargs={'username': 'Antho'})
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'profiles/profile.html')



