from clientes import Classic, Gold, Black, Cliente
from reporte import Reporte

class Razon:
    def __init__(self, cliente):
        self.reporte = Reporte(cliente)

    def resolver_problemas(self, cliente, transaccion):
        
        if transaccion['estado'] == "RECHAZADA":
        #TIPOS DE TRANSACCIONES
            if transaccion['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":

                self.__retiro_efectivo_cajero_automatico(cliente, transaccion)
            
            elif transaccion['tipo'] == "ALTA_TARJETA_CREDITO":
            
                self.__alta_tarjeta_credito(cliente, transaccion)
            
            elif transaccion['tipo'] == 'ALTA_CHEQUERA':
            
                self.__alta_chequera(cliente,transaccion)           
            
            elif transaccion['tipo'] == 'COMPRAR_DOLAR':
            
                self.__comprar_dolares(cliente,transaccion)
            
            elif transaccion['tipo'] == 'TRANSFERENCIA_ENVIADA':
            
                self.__enviar_transferencia(cliente,transaccion)
            
            elif transaccion['tipo'] == 'TRANSFERENCIA_RECIBIDA':
            
                self.__recibir_transferencia(cliente,transaccion)
        else:
            self.reporte.crear_reporte(transaccion, "")
   
   #FUNCION PARA RETIRAR EFECTIVO
    def __retiro_efectivo_cajero_automatico(self, cliente, transaccion):
        if transaccion['monto'] > cliente.obtener_cuenta().obtener_limite_extraccion():
            error = ("El monto es mayor al que se permite")

        elif transaccion['monto'] > transaccion['cupoDiarioRestante']:
            error = ("El monto supera lo que le queda por extraer")

        elif transaccion['monto'] > transaccion['saldoEnCuenta']:
            error = ("El monto es mayor al saldo")

        self.reporte.crear_reporte(transaccion, error)
    
    #FUNCION PARA PEDIR TARJETA DE CREDITO
    def __alta_tarjeta_credito(self, cliente, transaccion):
        
        if not cliente.puede_crear_tarjeta_credito():
            error = "No puede tener tarjetas de credito"

        elif transaccion['totalTarjetasDeCreditoActualmente'] + 1 > cliente.getCantTarjetas():
            error = "No puede tener mas tarjetas de credito"

        self.reporte.crear_reporte(transaccion, error)        
    
    #FUNCION PARA PEDIR CHEQUERA
    def __alta_chequera(self, cliente, transaccion):

        if not cliente.puede_crear_chequera():
            error = 'No esta habilitado para solicitar una chequera '

        elif transaccion['totalChequerasActualmente'] == cliente.getCantChequera():
            error = 'No puede tener mas chequeras '
        
        self.reporte.crear_reporte(transaccion, error)

    #FUNCION PARA COMPRAR DOLARES
    def __comprar_dolares(self, cliente, transaccion):
        if not cliente.puede_comprar_dolares():
            error = 'No esta habilitado para comprar dolares'

        elif transaccion['monto'] > transaccion['saldoEnCuenta']:
            error = "No hay saldo suficiente en la cuenta"

        self.reporte.crear_reporte(transaccion, error)

    #FUNCION PARA REALIZAR UNA TRANSFERENCIA
    def __enviar_transferencia (self,cliente,transaccion):

        if transaccion['monto'] + transaccion['monto'] * cliente.obtener_cuenta().obtener_costo_transferecia() > transaccion['saldoEnCuenta']:
            error = 'No puede transferir por saldo insuficiente'
        
        self.reporte.crear_reporte(transaccion, error)

    #FUNCION PARA RECIBIR UNA TRANSFERENCIA
    def __recibir_transferencia(self,cliente,transaccion):
        if transaccion['monto'] > cliente.obtener_cuenta().obtener_limite_transferencia_recibida():
            error = 'No puede recibir ese monto sin previo aviso'

        self.reporte.crear_reporte(transaccion, error)
        
#ACLARACION 1: SE PUEDE CREAR UN METODO APARTE QUE SEA EL ENCARGADO DE IMPRIMIR EN EL HTML
#ACLARACION 2: TODOS ESTOS METODOS QUE TIENEN QUE CREAR TIENEN QUE SER PRIVADOS PARA ESO PONEN "__" ADELANTE DEL NOMBRE DE LA FUNCION
#ejemplo: def __ejemplo_funcion(self):