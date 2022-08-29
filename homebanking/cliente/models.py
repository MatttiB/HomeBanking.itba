from django.db import models
from django.contrib.auth.models import User
from .choices import tipo_cliente

# Create your models here.
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = "auth_user"

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
    
class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_column='usuario' , null=True, blank=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    nacimiento = models.DateField()
    direccion = models.OneToOneField(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    idcuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, null=True, blank=True)
    idsucursal = models.OneToOneField(Sucursal, on_delete=models.CASCADE, null=True)
