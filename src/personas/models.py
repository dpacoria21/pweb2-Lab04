from django.db import models

# Create your models here.
# 2do commit
class Persona(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    edad = models.TextField()