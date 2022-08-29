from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"sucursales", SucursalViewSet)
router.register(r"cliente", ClienteViewSet, basename="cliente")
router.register(r"usuarios", UserViewSet, basename="usuarios")

urlpatterns = [
    path("", include(router.urls))
]