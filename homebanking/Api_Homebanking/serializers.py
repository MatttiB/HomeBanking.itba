from rest_framework import serializers
from cliente.models import Cliente, Cuenta, Direccion, Tarjeta, Sucursal, Sujetodireccion, Tiposcliente
from prestamo.models import Prestamo
from django.contrib.auth.models import User

# from homebanking.Clientes.models import Sujetodireccion


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    # usuario = serializers.HyperlinkedRelatedField(many=True, view_name="user-list", read_only=True)
    # iddirecciones = serializers.HyperlinkedRelatedField(many=True, view_name="Sujetodireccion-list", read_only=True)

    class Meta:
        model = Cliente
        fields = "all"


class SujetoDireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sujetodireccion
        fields = "all"


class TiposclienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tiposcliente
        fields = "all"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "all"


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = "all"


class PrestamosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = "all"


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "all"


class DireccionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = "all"


class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = "all"