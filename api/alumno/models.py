from django.db import models

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=140)
    apellidos = models.CharField(max_length=140)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50)
    dirección = models.CharField(max_length=140)
    carrera = models.CharField(max_length=50)
    

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=140)
# Create your models here.
