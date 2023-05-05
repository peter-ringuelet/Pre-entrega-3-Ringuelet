from django.db import models

# Create your models here.
class ComisionDirectiva(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    cargo = models.CharField(max_length=30)

class Socio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()

class Actividad(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_inicio = models.DateField()