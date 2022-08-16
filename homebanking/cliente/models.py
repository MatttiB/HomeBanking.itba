from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    nro_calle = models.CharField(max_length=255)
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    nacimiento = models.DateField()
    direccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)
