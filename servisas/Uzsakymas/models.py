from django.db import models

# Create your models here.

class Uzsakymas(models.Model):
    Data = models.DateField(null = True, help_text = "Gimimo data" )
    Automobilis_ID = models.ForeignKey(
                                # Automobilis,
                                # on_delete = models.CASCADE
    )
    Suma = models.models.IntegerField(_(""))