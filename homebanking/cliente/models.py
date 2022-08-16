from django.db import models
from django.contrib.auth.models import User
from .choices import tipo_cliente

# Create your models here.
class Cuenta(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=20, choices=tipo_cliente, default='C')
    saldo = models.IntegerField(default=0)

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    nro_calle = models.CharField(max_length=255)
    
    def __str__(self):
        return '{} {}, {}'.format(self.calle, self.nro_calle, self.provincia)
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    nacimiento = models.DateField()
    iddireccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    idcuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, null=True, blank=True)
