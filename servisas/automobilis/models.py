from django.db import models

# Create your models here.
class Auto(models.Model):
    Marke = models.CharField(max_length= 80)
    MOdelis = models.CharField(max_length= 80)
    Valstybinis = models.CharField(max_length= 80)
    VIN_kodas = models.CharField(max_length= 80)
    Klientas = models.CharField(max_length= 80)