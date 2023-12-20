from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Addres(models.Model):
    """La classe Adresse représente le modèle d'une adresse"""
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}' 
    
    class Meta:
        db_table = 'oc_lettings_site_address'


class Letting(models.Model):
    """La classe représente le modèle d'une location"""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Addres, on_delete=models.CASCADE)

    def __str__(self):
        return  self.title
    
    class Meta:
        db_table = 'oc_lettings_site_letting'
