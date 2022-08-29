from django.shortcuts import render, redirect
from .forms import FormularioRegistro, FormularioCliente, FormularioDireccion
from cliente.models import Cliente, Cuenta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = [FormularioRegistro(request.POST), FormularioCliente(request.POST), FormularioDireccion(request.POST)]
        
        if form[0].is_valid() and form[1].is_valid() and form[2].is_valid():
            direccion = form[2].save()
            user = form[0].save()
            cuenta = Cuenta()
            cuenta.save()
            
            cliente= Cliente(nombre=request.POST.get("nombre"),
                             apellido=request.POST.get("apellido"),
                             dni=request.POST.get("dni"),
                             nacimiento=request.POST.get("nacimiento"),
                             user = user,
                             iddireccion = direccion,
                             idcuenta= cuenta)
            cliente.save()
            
            login(request, user)
            return redirect("/inicio")
            
    else:
        form = form = [FormularioRegistro(), FormularioCliente(), FormularioDireccion()]
        
    return render(request, 'registration/registro.html', {"form_user": form[0],
                                                          "form_cliente": form[1],
                                                          "form_direccion": form[2]})