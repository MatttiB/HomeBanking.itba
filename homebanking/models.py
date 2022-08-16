# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    iddirecciones = models.ForeignKey('Sujetodireccion', models.DO_NOTHING, db_column='idDirecciones', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField()
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    limiteextracciondiario = models.TextField(db_column='limiteExtraccionDiario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    limitetransferenciarecibida = models.TextField(db_column='limiteTransferenciaRecibida', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    costortransferenciarecibida = models.TextField(db_column='costorTransferenciaRecibida', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    saldodescubiertodisponible = models.TextField(db_column='saldoDescubiertoDisponible', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tipocuenta = models.TextField(db_column='tipoCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    iddireccion = models.AutoField(db_column='idDireccion', blank=True, null=True)  # Field name made lowercase.
    calle = models.TextField()
    numero = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    iddirecciones = models.ForeignKey('Sujetodireccion', models.DO_NOTHING, db_column='idDirecciones')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'direcciones'


class Empleado(models.Model):
    employee_id = models.AutoField()
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
    iddirecciones = models.ForeignKey('Sujetodireccion', models.DO_NOTHING, db_column='idDirecciones', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'


class Marcastarjeta(models.Model):
    marcaid = models.AutoField(db_column='marcaID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    nombremarca = models.TextField(db_column='nombreMarca')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marcasTarjeta'


class Movimientos(models.Model):
    movimientoid = models.AutoField(db_column='movimientoID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    account_id = models.IntegerField()
    monto = models.IntegerField()
    tipomovimiento = models.TextField(db_column='tipoMovimiento')  # Field name made lowercase.
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField()
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    iddirecciones = models.ForeignKey('Sujetodireccion', models.DO_NOTHING, db_column='idDirecciones', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sucursal'


class Sujetodireccion(models.Model):
    iddirecciones = models.AutoField(db_column='idDirecciones', primary_key=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sujetoDireccion'


class Tarjeta(models.Model):
    numerotarjeta = models.TextField(db_column='numeroTarjeta')  # Field name made lowercase.
    marcaid = models.ForeignKey(Marcastarjeta, models.DO_NOTHING, db_column='marcaID')  # Field name made lowercase.
    cvv = models.TextField(db_column='CVV')  # Field name made lowercase.
    fechaotorgamiento = models.TextField(db_column='fechaOtorgamiento')  # Field name made lowercase.
    fechaexpiracion = models.TextField(db_column='fechaExpiracion')  # Field name made lowercase.
    tipotarjetaid = models.ForeignKey('Tipotarjeta', models.DO_NOTHING, db_column='tipoTarjetaID')  # Field name made lowercase.
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'


class Tipotarjeta(models.Model):
    tipotarjetaid = models.AutoField(db_column='tipoTarjetaID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    nombretipo = models.TextField(db_column='nombreTipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoTarjeta'


class Tiposcliente(models.Model):
    tipoid = models.AutoField(db_column='tipoID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    cantidadmaxchequeras = models.IntegerField(db_column='cantidadMaxChequeras')  # Field name made lowercase.
    cantidadmaxtarjetas = models.IntegerField(db_column='cantidadMaxTarjetas')  # Field name made lowercase.
    puedecrearchequera = models.IntegerField(db_column='puedeCrearChequera')  # Field name made lowercase.
    puedecreartarjetacredito = models.IntegerField(db_column='puedeCrearTarjetaCredito')  # Field name made lowercase.
    puedecomprardolar = models.IntegerField(db_column='puedeComprarDolar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiposCliente'