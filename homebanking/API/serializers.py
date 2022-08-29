from cgitb import lookup
from django.http import Http404
from rest_framework import serializers
from cliente.models import *
from tarjeta.models import *
from prestamo.models import Prestamo
from django.contrib.auth.models import User
from datetime import datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class DireccionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    direccion_pais = serializers.CharField(source='direccion.pais',read_only=True)
    direccion_provincia = serializers.CharField(source='direccion.provincia',read_only=True)
    direccion_ciudad = serializers.CharField(source='direccion.ciudad',read_only=True)
    direccion_calle = serializers.CharField(source='direccion.calle',read_only=True)
    direccion_nro_calle = serializers.CharField(source='direccion.nro_calle',read_only=True)
    idcuenta = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "dni", "nacimiento", 'direccion_pais', 'direccion_provincia', 'direccion_ciudad', 'direccion_calle', 'direccion_nro_calle', 'idcuenta']


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['saldo', 'tipo_cuenta']


class PrestamosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['tipo_prestamo', 'monto']

class PrestamosTotalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['sucursal', 'monto']

class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Tarjeta
        fields = ['idtarjeta', 'cliente']

class TratamientoPrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'

    def create(self, validated_data):
        cuenta = Cuenta.objects.get(id_cuenta=validated_data["cuenta"].id_cuenta)
        if cuenta:
            cuenta.saldo += int(validated_data["monto"])
            cuenta.save()
        else:
            raise Http404
        validated_data["fecha_inicio"] = datetime.now().strftime("%Y-%m-%d")
        return Prestamo.objects.create(**validated_data)

    def destroy(self, validated_data):
        cuenta = Cuenta.objects.get(id_cuenta=validated_data["cuenta"].id_cuenta)
        if cuenta:
                cuenta.saldo -= int(validated_data["monto"])
                cuenta.save()
        else:
                raise Http404
        return Prestamo.objects.delete(**validated_data)

class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"