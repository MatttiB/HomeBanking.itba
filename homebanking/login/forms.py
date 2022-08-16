from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cliente.models import Cliente,Direccion

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "dni", "nacimiento"]
        
        widgets = {'nacimiento': forms.DateInput(attrs={'type': 'date'})}
        
class FormularioDireccion(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ["pais", "provincia", "ciudad", "calle", "nro_calle"]
        