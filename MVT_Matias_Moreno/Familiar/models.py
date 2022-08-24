from pyexpat import model
from django.db import models

# Create your models here.
class Familiar(models.Model):

    nombre = models.CharField(max_length=30)
    años = models.FloatField()
    fecha_de_nacimiento = models.DateField()
