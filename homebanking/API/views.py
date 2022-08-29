from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from .serializers import *
from cliente.models import *
from tarjeta.models import *
from prestamo.models import Prestamo
from django.contrib.auth.models import User

# Create your views here.

class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request):
        queryset = User.objects.get(username=request.user)
        serializer = UserSerializer(queryset, many=False, context={"request": request})
        return Response(serializer.data)

class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
    
    def list(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            pass
        else:
            queryset = Cliente.objects.get(direccion=usuario.cliente.direccion)
            serializer = ClienteSerializer(queryset, many=False, context={"request": request})
        
        return Response(serializer.data)