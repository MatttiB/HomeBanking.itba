from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from .serializers import ClienteSerializer, UserSerializer, SujetoDireccionSerializer, TiposclienteSerializer
from cliente.models import Cliente, Sujetodireccion, Tiposcliente
from django.contrib.auth.models import User

# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        usuario = User.objects.get(username=request.user)
        queryset = Cliente.objects.get(usuario=usuario.id)
        serializer = ClienteSerializer(queryset, many=False, context={"request": request})
        return Response(serializer.data)


class SujetoDireccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sujetodireccion.objects.all()
    serializer_class = SujetoDireccionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TiposclienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tiposcliente.objects.all()
    serializer_class = TiposclienteSerializer
    permission_classes = [permissions.IsAuthenticated]