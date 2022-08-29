from multiprocessing import context
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

class CuentaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'patch']
    
    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Direccion.objects.filter(pk=pk)
            serializer = DireccionesSerializer(queryset, many=True, context={"request": request})
            if serializer.data:
                return Response(serializer.data)
            return Response({"detail": "La direccion no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            cliente = Cliente.objects.get(usuario=usuario.id)
            queryset = Direccion.objects.get(pk=pk)
            print(queryset.iddirecciones)
            print(cliente.iddirecciones)
            if queryset.iddirecciones == cliente.iddirecciones:
                serializer = DireccionesSerializer(queryset, many=False, context={"request": request})
                return Response(serializer.data)
            return Response({"detail": "Solo puedes acceder a tus direcciones"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def list(self, request):
        usuario = User.objects.get(username=request.user)
        cliente = usuario.cliente
        queryset = Cuenta.objects.get(id_cuenta=cliente.idcuenta_id)
        serializer = CuentaSerializer(queryset, many=False, context={'request':request})
        return Response(serializer.data)
    
class PrestamoViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Prestamo.objects.all()
    http_method_names = ['get']
    
    def list(self, request):
        usuario = User.objects.get(username=request.user)
        
        if usuario.is_staff:
            queryset = Prestamo.objects.all()
            serializer = PrestamosTotalSerializer(queryset, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            cliente = usuario.cliente
            queryset = Prestamo.objects.filter(cuenta=cliente.idcuenta_id)
            serializer = PrestamosSerializer(queryset, many=True, context={'request':request})
            return Response(serializer.data)
        
    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        
        if usuario.is_staff:
            queryset = Prestamo.objects.filter(sucursal=pk)
            serializer = PrestamosSerializer(queryset, many=True, context={"request": request})
            if serializer.data:
                return Response(serializer.data)
            return Response({"detail": "La sucursal no tiene prestamos"}, status=status.HTTP_404_NOT_FOUND)
        return Response(
            {"detail": "No tiene permisos para acceder a esta información"}, status=status.HTTP_401_UNAUTHORIZED
        )
            
class TarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TarjetaSerializer
    queryset = Tarjeta.objects.all()
    http_method_names = ['get']
    
    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        
        if usuario.is_staff:
            queryset = Tarjeta.objects.filter(cliente_id=pk)
            serializer = TarjetaSerializer(queryset, many=True, context={"request": request})
            if serializer.data:
                return Response(serializer.data)
            return Response({"detail": "El cliente no tiene tarjetas"}, status=status.HTTP_404_NOT_FOUND)
        return Response(
            {"detail": "No tiene permisos para acceder a esta información"}, status=status.HTTP_401_UNAUTHORIZED
        )
        
class DireccionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Direccion.objects.all()
    serializer_class = DireccionesSerializer
    http_method_names = ['put', 'get']

    def list(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
        
            queryset = Direccion.objects.all()
            serializer = DireccionesSerializer(queryset, context={'request':request})
            return Response(serializer.data)
        
        else:
            
            cliente = usuario.cliente
            queryset = Direccion.objects.get(id_direccion=cliente.direccion_id)
            serializer = DireccionesSerializer(queryset, many=False, context={"request":request})
            
            if serializer.data:
                return Response(serializer.data)
            return Response({'detail':'El cliente no tiene direccion'}, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None, partial=True):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            instance = self.get_object()
            serializer = DireccionesSerializer(
                instance, data=request.data, partial=partial, context={"request": request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            cliente = Cliente.objects.get(user_id=usuario.id)
            instance = self.get_object()
            serializer = DireccionesSerializer(
                instance, data=request.data, partial=partial, context={"request": request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TratamientoPrestamoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Prestamo.objects.all()
    serializer_class = TratamientoPrestamosSerializer
    http_method_names = ["post", "delete"]

    def create(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            serializer = self.serializer_class(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            instance = self.get_object()
            print(instance)
            cuenta = Cuenta.objects.get(id_cuenta=instance.cuenta.id_cuenta)
            if cuenta:
                cuenta.saldo -= int(instance.monto)
                cuenta.save()
            else:
                raise Http404
            instance.delete()
            return Response({"detail": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_401_UNAUTHORIZED)
