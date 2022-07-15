class Razon:
    def __init__(self):
        pass
    
    def resolver_problemas(self, cliente, transaccion):
        if transaccion['estado'] == "RECHAZADA":
            """aca va analizar el porque fue rechazada dependiendo de la accion que se quizo hacer
                para eso pueden crear distintos metodos o que analicen los diferentes tipos de acciones y terminen imprimiendo
                en el html lo que piden
            """
            pass
        else:
            """
                en el caso de que sea ACEPTADA no se analiza nada y se imprime lo que pide en el html
            """
            pass
        
#ACLARACION 1: SE PUEDE CREAR UN METODO APARTE QUE SEA EL ENCARGADO DE IMPRIMIR EN EL HTML
#ACLARACION 2: TODOS ESTOS METODOS QUE TIENEN QUE CREAR TIENEN QUE SER PRIVADOS PARA ESO PONEN "__" ADELANTE DEL NOMBRE DE LA FUNCION
#ejemplo: def __ejemplo_funcion(self):