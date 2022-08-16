from django.contrib import admin
from .models import Cliente,Direccion,Cuenta
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Cuenta)