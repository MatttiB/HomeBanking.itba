from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cliente
        field = 'all'
        
class CuentaSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model = models.Cuenta
        field = 'all'
        
class DireccionSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model = models.Direccion
        field = 'all'