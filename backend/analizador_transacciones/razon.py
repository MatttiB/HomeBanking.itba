from clientes import Classic, Gold, Black, Cliente

class Razon:
    def __init__(self):
        pass    

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
            elif transaccion['tipo'] == 'TRANSFERENCIA_ENVIADA:':
                self.__enviar_transferencia(cliente,transaccion)
            elif transaccion['tipo'] == 'TRANSFERENCIA_RECIBIDA:':
                self.__recibir_transferencia(cliente,transaccion)
        else:
            pass
        return cliente
   
   #FUNCION PARA RETIRAR EFECTIVO
    def __retiro_efectivo_cajero_automatico(self, cliente, transaccion):
        if transaccion['monto'] > cliente.obtener_retiro_max_diario():
            print("el monto es mayor al que se permite")

        elif transaccion['monto'] > transaccion['cupoDiarioRestante']:
            print("el monto supera lo que le queda por extraer")

        elif transaccion['monto'] > transaccion['saldoEnCuenta']:
            print("el monto es mayor al saldo")
    
    #FUNCION PARA PEDIR TARJETA DE CREDITO
    def __alta_tarjeta_credito(self, cliente, transaccion):
        
        if cliente.puede_crear_tarjeta_credito()=='false':
            print("No puede tener tarjetas de credito")

        elif transaccion['totalTarjetasDeCreditoActualmente'] == cliente.getCantTarjetas():
            print("No puede tener mas tarjetas de credito")        
    
    #FUNCION PARA PEDIR CHEQUERA
    def __alta_chequera(self, cliente, transaccion):

        if cliente.puede_crear_chequera()=='false':
            print('No esta habilitado para solicitar una chequera ')

        elif transaccion['totalChequerasActualmente'] == cliente.getCantChequera():
            print('No puede tener mas chequeras ')

    #FUNCION PARA COMPRAR DOLARES
    def __comprar_dolares(self, cliente):
        if cliente.puede_comprar_dolares()=='false':
            print('No esta habilitado para comprar dolares')

    #FUNCION PARA REALIZAR UNA TRANSFERENCIA
    def __enviar_transferencia (self,cliente,transaccion):

        if transaccion['monto'] > transaccion['saldoEnCuenta']:
            print("No tiene dinero disponible para transferir")

        elif cliente['tipo'] == 'Classic':
            if transaccion['monto']+ transaccion['monto']*0.01 > transaccion['saldoEnCuenta']:
                 print ('No puede transferir, saldo insuficiente')

        elif cliente['tipo'] == 'Gold':
            if transaccion['monto']+ transaccion['monto']*0.005 > transaccion['saldoEnCuenta']:
                 print ('No puede transferir, saldo insuficiente')
    
    #FUNCION PARA RECIBIR UNA TRANSFERENCIA
    def __recibir_transferencia(self,cliente,transaccion):
        if cliente['tipo'] == 'Classic' and transaccion['monto'] > 150000:
            print ('No puede recibir ese monto sin previo aviso')
        elif cliente['tipo'] == 'Gold' and transaccion['monto'] > 500000:
            print ('No puede recibir ese monto sin previo aviso')
        
#ACLARACION 1: SE PUEDE CREAR UN METODO APARTE QUE SEA EL ENCARGADO DE IMPRIMIR EN EL HTML
#ACLARACION 2: TODOS ESTOS METODOS QUE TIENEN QUE CREAR TIENEN QUE SER PRIVADOS PARA ESO PONEN "__" ADELANTE DEL NOMBRE DE LA FUNCION
#ejemplo: def __ejemplo_funcion(self):