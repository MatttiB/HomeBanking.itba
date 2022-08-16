from .models import Prestamo
from django import forms

class FormularioPrestamo(forms.ModelForm):
    
    class Meta:
        model = Prestamo
        fields = ["monto", "tipo_prestamo", "fecha_inicio"]
        
        widgets = {'fecha_inicio': forms.DateInput(attrs={'type': 'date'})}