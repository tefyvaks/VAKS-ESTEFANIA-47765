from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Libro(models.Model):
    titulo= models.CharField(max_length=40)
    autor= models.CharField(max_length=40)
    genero= models.CharField(max_length=40)
    marca = models.CharField(max_length=50, default="Desconocida")
    descripcion = models.TextField(default="Sin descripción disponible")
    year= models.IntegerField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Pelicula(models.Model):
    titulo= models.CharField(max_length=40)
    autor= models.CharField(max_length=40)
    genero= models.CharField(max_length=40)

class Musica(models.Model):
    titulo= models.CharField(max_length=40)
    autor= models.CharField(max_length=40)
    genero= models.CharField(max_length=40)
    
