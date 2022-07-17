from clientes import Classic, Gold, Black
from razon import Razon
import json
import argparse

parser = argparse.ArgumentParser(description= "Analizador de transacciones")
parser.add_argument('NOMBRE_ARCHIVO', type=str, help='El nombre del archivo en el que se tiene que buscar')

archivo = parser.parse_args()

with open(archivo.NOMBRE_ARCHIVO, 'r') as archivo:
    datos_cliente = json.load(archivo)
    
    if datos_cliente['tipo'] == 'CLASSIC':
    
        cliente = Classic(datos_cliente, "CLASSIC")
    
    elif datos_cliente['tipo'] == 'GOLD':
    
        cliente = Gold(datos_cliente, "GOLD")
    
    else:
        
        cliente = Black(datos_cliente, "BLACK")
    
    razon = Razon(cliente)
    
    for transaccion in datos_cliente.get('transacciones'):
        razon.resolver_problemas(cliente, transaccion)
    