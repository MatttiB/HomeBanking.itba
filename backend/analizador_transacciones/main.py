from clientes import Classic, Gold, Black
from razon import Razon
import json

with open('eventos_classic.json', 'r') as archivo:
    razon = Razon()
    datos_cliente = json.load(archivo)
    
    if datos_cliente['tipo'] == 'CLASSIC':
    
        cliente = Classic(datos_cliente)
    
    elif datos_cliente['tipo'] == 'GOLD':
    
        cliente = Gold(datos_cliente)
    
    else:
        
        cliente = Black(datos_cliente)
    
    for transaccion in datos_cliente.get('transacciones'):
        razon.resolver_problemas(cliente, transaccion)
    