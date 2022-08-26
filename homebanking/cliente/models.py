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

class AuditoriaCuenta(models.Model):
    auditoria_id = models.AutoField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.IntegerField(blank=True, null=True)
    new_iban = models.IntegerField(blank=True, null=True)
    old_type = models.IntegerField(blank=True, null=True)
    new_type = models.IntegerField(blank=True, null=True)
    user_action = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "auditoria_cuenta"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


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


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column="employee_DNI")  # Field name made lowercase.
    branch_id = models.IntegerField()
    iddirecciones = models.ForeignKey(
        "Sujetodireccion", on_delete=models.CASCADE, db_column="idDirecciones", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "empleado"


class Marcastarjeta(models.Model):
    marcaid = models.AutoField(db_column="marcaID", primary_key=True)  # Field name made lowercase.
    nombremarca = models.TextField(db_column="nombreMarca")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "marcasTarjeta"


class Movimientos(models.Model):
    movimientoid = models.AutoField(db_column="movimientoID", primary_key=True)  # Field name made lowercase.
    account_id = models.IntegerField()
    monto = models.IntegerField()
    tipomovimiento = models.TextField(db_column="tipoMovimiento")  # Field name made lowercase.
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = "movimientos"


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    iddirecciones = models.ForeignKey(
        "Sujetodireccion", on_delete=models.CASCADE, db_column="idDirecciones", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "sucursal"


class Sujetodireccion(models.Model):
    iddirecciones = models.AutoField(db_column="idDirecciones", primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "sujetoDireccion"


class Tarjeta(models.Model):
    numerotarjeta = models.TextField(db_column="numeroTarjeta", primary_key=True)  # Field name made lowercase.
    marcaid = models.ForeignKey(
        Marcastarjeta, on_delete=models.CASCADE, db_column="marcaID"
    )  # Field name made lowercase.
    cvv = models.TextField(db_column="CVV")  # Field name made lowercase.
    fechaotorgamiento = models.TextField(db_column="fechaOtorgamiento")  # Field name made lowercase.
    fechaexpiracion = models.TextField(db_column="fechaExpiracion")  # Field name made lowercase.
    tipotarjetaid = models.ForeignKey(
        "Tipotarjeta", on_delete=models.CASCADE, db_column="tipoTarjetaID"
    )  # Field name made lowercase.
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column="customer_id")

    class Meta:
        managed = False
        db_table = "tarjeta"


class Tipotarjeta(models.Model):
    tipotarjetaid = models.AutoField(db_column="tipoTarjetaID", primary_key=True)  # Field name made lowercase.
    nombretipo = models.TextField(db_column="nombreTipo")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tipoTarjeta"


class Tiposcliente(models.Model):
    tipoid = models.AutoField(db_column="tipoID", primary_key=True)  # Field name made lowercase.
    nombretipo = models.TextField(db_column="nombreTipo")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tiposCliente"