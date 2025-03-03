from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """La classe représente le modèle d'un profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        managed = False
        db_table = 'oc_lettings_site_profile'