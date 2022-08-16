from django.urls import path
from . import views

urlpatterns = [
    path("", views.prestamos, name="prestamos")
]