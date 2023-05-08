from django.db import models

# Create your models here.
class ComisionDirectiva(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    cargo = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Cargo: {self.cargo}"

class Socio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni}"

class Actividad(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Fecha Inicio: {self.fecha_inicio}"
    
