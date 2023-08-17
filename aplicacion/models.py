from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entegado = models.BooleanField()