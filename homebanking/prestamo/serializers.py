from dataclasses import field
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class PrestamoSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model = models.Prestamo
        field = 'all'