from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"sucursales", SucursalViewSet)
router.register(r"cliente", ClienteViewSet, basename="cliente")
router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r'direccion', DireccionViewSet, basename='direccion')
router.register(r'cuenta', CuentaViewSet, basename='cuenta')
router.register(r'prestamos', PrestamoViewSet, basename='prestamo')
router.register(r'tarjetas', TarjetaViewSet, basename='tarjetas')
router.register(r'tratamiento_prestamos', TratamientoPrestamoViewSet, basename='tratamiento_prestamo')

urlpatterns = [
    path("", include(router.urls))
]