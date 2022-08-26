from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from Clientes.models import Cuenta, Tarjeta, Cliente


# Create your views here.


def homebanking(request):
    try:
        request.session["usuario"]
        cuentasCliente = Cuenta.objects.filter(customer_id=request.session["customer_id"])
        cantidadCuentas = len(list(cuentasCliente))
        customer_name = request.session["customer_name"]
        customer_surname = request.session["customer_surname"]
        tarjetas = Tarjeta.objects.filter(customer_id=request.session["customer_id"])

        context = {
            "customer_name": customer_name,
            "customer_surname": customer_surname,
            "cuentasCliente": cuentasCliente,
            "cantidadCuentas": cantidadCuentas,
            "tarjetas": tarjetas,
        }
        return render(request, "Cuentas/homebanking.html", context=context)
    except (Session.DoesNotExist, KeyError):
        return redirect("/")


def gastos(request):
    try:
        request.session["usuario"]
        return render(request, "Cuentas/gastos.html")
    except (Session.DoesNotExist, KeyError):
        return redirect("/")