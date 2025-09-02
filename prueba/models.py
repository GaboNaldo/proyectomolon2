from django.db import models

# Create your models here.
class Perro(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    
    
