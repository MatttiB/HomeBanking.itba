from cgitb import lookup
from rest_framework import serializers
from cliente.models import *
from tarjeta.models import *
from prestamo.models import Prestamo
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class DireccionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ["id_direccion", "pais", "provincia", "ciudad", "calle", "nro_calle"]

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    direccion = serializers.StringRelatedField()
    idcuenta = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "dni", "nacimiento", 'direccion', 'idcuenta']


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"


class PrestamosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"


class TotalPrestamosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"



class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"