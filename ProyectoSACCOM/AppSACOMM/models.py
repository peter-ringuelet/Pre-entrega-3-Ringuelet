from django.db import models

# Create your models here.
class ComisionDirectiva(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    cargo = models.CharField(max_length=30)

class Socio(models.Model):
    