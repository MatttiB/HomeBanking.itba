from ast import For
from django.shortcuts import render, redirect
from .forms import FormularioRegistro
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/inicio")
            
    else:
        form = FormularioRegistro()
        
    return render(request, 'registration/registro.html', {"form": form})