from django.shortcuts import render
from cliente.models import Cuenta
# Create your views here.
def inicio(request):
    return render(request, 'cuenta/inicio.html')