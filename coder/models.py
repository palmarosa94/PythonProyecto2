from django.db import models

# Create your models here.

class Abogados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    nro_abogado = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"Abogado: {self.nombre} - Nro. de abogado: {self.nro_abogado}"
    
class Peritos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    nro_perito = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"Perito: {self.nombreombre} - Nro. de perito: {self.nro_abogado}"

class Jurisdicciones(models.Model):
    localidad= models.CharField(max_length=100)
    provincia= models.CharField(max_length=100)
    codigo= models.CharField(max_length=3, unique=True)
    
    
 