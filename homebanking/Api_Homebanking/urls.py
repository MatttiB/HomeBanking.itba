from django.contrib import admin
from django.urls import path, include

from .views import ClienteViewSet, UserViewSet, SujetoDireccionViewSet, TiposclienteViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"cliente", ClienteViewSet, basename="cliente")
router.register(r"usuarios", UserViewSet)
router.register(r"direcciones", SujetoDireccionViewSet)
router.register(r"tipoCliente", TiposclienteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]