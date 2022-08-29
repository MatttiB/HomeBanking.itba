from django.db import models
from cliente.models import Cuenta, Sucursal

# Create your models here.
class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    monto = models.IntegerField()
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tipo_prestamo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True)