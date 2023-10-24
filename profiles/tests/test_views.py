from profiles.models import Profile
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class TestView(TestCase):
    client = Client()

    def test_indexProfile(self):
        response = self.client.get('/profiles/')
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertEqual(response.status_code, 200)
    
    def test_profiles(self):
        user = User.objects.create(username='Antho')
        profile = Profile.objects.create(user=user, favorite_city='maurecourt')
        path = reverse('profile', kwargs={'username': 'Antho'})
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.status_code, 200)



