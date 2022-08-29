from django.db import models
from cliente.models import Cliente
# Create your models here.

class Tarjeta(models.Model):
    idtarjeta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)